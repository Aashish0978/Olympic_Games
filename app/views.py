from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import get_template
from. models import (About, Sport,
                      SportsCategory, Match, 
                      News, Blogs, Contact, ResultsAndHighlights,
                      Atheletes, Booking,UserDetails, Gallery, 
                      Streaming, Comment)
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.forms import (PasswordChangeForm, PasswordResetForm,
                                       UserCreationForm)
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.paginator import Paginator
from django .contrib import messages
from django .contrib.messages import get_messages
from xhtml2pdf import pisa   
import datetime
import random
from io import BytesIO
from .utils import render_to_pdf
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import (DjangoUnicodeDecodeError, force_bytes,
                                   smart_str)
from .utlis import Util
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from reportlab.pdfgen import canvas
from .forms import ContactForm, ValidateForm
from django.contrib import sessions



# Create your views here.
def index(request):
    matches= Match.objects.all()[:2]
    gallery= Gallery.objects.all()[:3]
    post= Gallery.objects.all()[:6]

    return render(request, 'app/index.html',{'matches':matches,'gallery':gallery})

def about(request):
    data = About.objects.all()
    return render(request, 'app/about.html', {'data': data})

def account(request):
    return render(request, 'app/account.html')

def contact(request):
    if request.method =="POST":
        form =ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            messages.success(request , "sucessful")
            return redirect("contact")
        else:
            messages.error(request, "error")
    else:
        contact = ContactForm()
        storage  = get_messages(request)

    # for message in storage:
    #     pass
        return render(request, 'app/contact.html',{'form':contact})

def gallery(request):
    gallery= Gallery.objects.all()
    paginator = Paginator(gallery,6)
    page_number = request.GET.get('page')
    gallery = paginator.get_page(page_number)
    return render(request, 'app/gallery.html', {'gallery':gallery})

def history(request):
    return render(request, 'app/history.html')

def atheletes(request):
    atheletes= Atheletes.objects.all()
    paginator = Paginator(atheletes,6)
    page_number = request.GET.get('page')
    atheletes = paginator.get_page(page_number)
    return render(request, 'app/atheletes.html', {'atheletes':atheletes})

def atheletes_details(request, slug):
    ath_details= Atheletes.objects.get(atheletes_slug=slug)
    return render(request,'app/atheletes_details.html',{'ath_details':ath_details})

def login(request):
    return render(request, 'app/login.html')

def leaguestandings(request):
    return render(request, 'app/league-standings.html')

def sport_relatedcategory(request, slug):
    sport_category= SportsCategory.objects.get(ctg_slug=slug)
    related_blogs=Sport.objects.filter(catagory=sport_category)
    paginator = Paginator(related_blogs,1)
    page_number = request.GET.get('page')
    related_blogs = paginator.get_page(page_number)
    return render(request,'app/sports.html',{'related_blogs':related_blogs,
                                             'sport':related_blogs})

def sports(request):
    sport= Sport.objects.all()
    paginator = Paginator(sport,4)
    page_number = request.GET.get('page')
    sport = paginator.get_page(page_number)
    return render(request, 'app/sports.html', {'sport':sport, 'related_blogs':sport})

def sport_details(request, slug):
    details= Sport.objects.get(blog_slug=slug)
    return render(request,'app/sport_details.html',{'detail':details})

def match_schedule(request):
    matches= Match.objects.all()
    paginator = Paginator(matches,3)
    page_number = request.GET.get('page')
    matches = paginator.get_page(page_number)
    return render(request, 'app/match_schedule.html', {'matches':matches})

def news(request):
    news= News.objects.all()
    return render(request, 'app/news.html', {'news':news})

def matchresult(request):
    result= ResultsAndHighlights.objects.all()
    return render(request, 'app/match_result.html', {'result':result})

def blogs(request):
    blog= Blogs.objects.all()
    return render(request, 'app/blogs.html', {'blog':blog})

def blogdetails(request, slug):
    blog_details= Blogs.objects.get(details_slug=slug)
    return render(request, 'app/blog_details.html', {'blog_details':blog_details})

def booking(request):
    if request.method =="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        country= request.POST['country']
        city= request.POST['city']
        pnumber= request.POST['phone']
        email= request.POST['email']
        person = request.POST['person']
        price =1500

        booking_info= Booking(firstname=fname,lastname=lname,
                              country=country,city=city,
                              phone=pnumber,email=email,
                              person =person)
        messages.success(request, "added Sucessfully")
        
        booking_info.save()

        template_name =get_template("app/invoice_pdf.html")
        templates_invoice ="app/pdf.html" 
        print(person)
        total = int(person) * 1500
        print(total)
        invoice_date =  datetime.datetime.now()  
        invoice_number = random.randint(1000, 9999)
        data ={
            'fullname':fname+" "+lname,
            'total':total,
            'person':person,
            'invoice_number':invoice_number,
            'invoice_create_date':invoice_date,
            'phonenumber':pnumber,
            'email':email,
            'location':city +" "+country,
            'price':1500
        }
        
        html  =template_name.render(data)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        pdf = result.getvalue()
        filename = "Match_booking_ticket_%s.pdf" %str(invoice_number)
        mail_subject = 'Invoice Details'
        template = get_template("app/invoice_pdf.html")
        message  = template.render(data)

        to_email =email
        email_from = settings.EMAIL_HOST_USER
        email = EmailMultiAlternatives(mail_subject,message,email_from,[to_email])
        email.attach_alternative(message, "text/html")
        email.attach(filename, pdf, 'application/pdf')
        email.send()
        



        # subject="booking info"
        # message=f"Thank you for Booking"
        # email_from= settings.EMAIL_HOST_USER
        # recipient_list= [email]
        # send_mail(subject,message,email_from,recipient_list)
    return render(request,'app/booking.html' )

def sign_in(request):
    if request.method =="POST":
        form = ValidateForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
           
            recaptcha_response =request.POST.get('g-recaptcha-response')
                
                # Perform reCAPTCHA verification
            from urllib import request as urllib_request
            import json

            recaptcha_secret_key = '6LcZ99UmAAAAAPXsBLLVI1ctkrZzw9UKsuWz_hmR'  # Replace with your reCAPTCHA secret key

            verification_url = 'https://www.google.com/recaptcha/api/siteverify'
            data = urllib_request.urlopen(f'{verification_url}?secret={recaptcha_secret_key}&response={recaptcha_response}').read()
            result = json.loads(data)
            print(result)

            if not result['success']:
                return render (request, 'app/sign_in.html', {'signin':"Invalid captcha!!",'form':ValidateForm()})
            if user.is_staff:
                auth.login(request, user)
                return redirect('admin/')
            auth.login(request, user)
            return redirect('index')
            

        # messages.warning(request,"Invalid username and pssword !")
        return render (request, 'app/sign_in.html', {'signin':"Invalid username or pssword !","form": ValidateForm()})
    
    return render (request, 'app/sign_in.html', {'form':ValidateForm()})


def custom_logout(request):
    user = request.user
    print(user)
    logout(request)
    return redirect(sign_in)

# def signup(request):
#     # if request.method == "POST":
#     #     fullname= request.POST['fullname']
#     #     email=  request.POST['email']
#     #     password= request.POST['password']
#     #     user = user(fullname=fullname, password1=password, email=email)
#     #     user.save()
#     #     return HttpResponse ("welcome")
#     # return render(request, 'app2/sign_up.html')

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('sign_in')
#     form = UserCreationForm()
#     return render(request, 'app/sign_up.html',{'form':form}) 

def signup(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password =request.POST['password']
    #     print(password)
    #     user = User(username=username, password=password,password2=password, email=email)
    #     user.save()
    #     print(" user login")
    #     return HttpResponse("welcome")
    # return render (request,  'app/registration.html')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        email=request.POST['email']
        if form.is_valid():
            form.save()
            user=User.objects.all()
            recent_user =user.last()
            print(recent_user)
            print(user)
            user_detail=UserDetails(email=email,user=recent_user)
            user_detail.save()
            return redirect('sign_in')
        else:
            return render (request,  'app/sign_up.html',{'form':form, 'signup':"Invalid error while credating user!!"})

    form= UserCreationForm()
    return render (request, 'app/sign_up.html',{'form':form})

@login_required(login_url='/sign_in')
def change_password(request):
    if request.method =="POST":
        user= request.user
        # password1 = request.POST['new_password1']
        # print(password1)
        form = PasswordChangeForm(request.user,request.POST)

        print(request.POST['new_password1'])
        if form.is_valid():
            form.save()
            return redirect('logout')
        else:
            return render(request, 'app/changepassword.html',{'form':form})
    form = PasswordChangeForm(request.user)
    return render(request, 'app/changepassword.html',{'form':form})


    
def streaming(request):
    video=Streaming.objects.first()
    comments=video.videos.all()
    print(comments)
    return render(request, 'app/streaming.html',{'streaming_video':video,'comments':comments})


def comments(request):
    if request.method=="POST":
     comments=request.POST['vido_cmt']
     videoid=request.POST['video']
     video=Streaming.objects.get(id=videoid)
     newcmt=Comment(comments=comments,video=video, person=request.user)
    #  messages.success(request, "added Sucessfully")
     newcmt.save()
     return redirect('streaming')
    else:
        return HttpResponse("not allowed")


def forgot_password(request):
    if request.method=="POST":
        email=request.POST['email']
        user=UserDetails.objects.get(email=email)
        print(user)
        relate_user = User.objects.get(username=user.user)
        print(relate_user)
        print(relate_user)
        
        
        # uid = urlsafe_base64_encode(force_bytes(relate_user.id))
        # print('Encoded UID', uid)
        token = PasswordResetTokenGenerator().make_token(relate_user)
        print('Password Reset Token', token)
        link = 'http://127.0.0.1:8000/reset/password/'+str(relate_user.id)+'/'+token
        print('Password Reset Link', link)
        # Send EMail
        body = 'Click Following Link to Reset Your Password '+link
        data = {
            'subject':'Reset Your Password',
            'body':body,
            'to_email':user.email
        }
        Util.send_email(data)
    
    return render (request, 'app/forgot_password.html')

def password_change(request):
    return render (request, 'app/password_change.html')

def restpasword(request, uid, token):
    id =int(uid)
    print(type(id),111111111111111111111111111111)
    print(id,22222222222222222222222222222222222222222222)
    if request.method =="POST":
        password =request.POST['password']
        password2= request.POST['password1']
        print(password, 33333333333333333333333333333333333333)
        print(password2, 33333333333333333333333333333333333333)
        if password == password2:
            user = User.objects.get(id= id)
            
            user.set_password(password)
            user.save()
            return HttpResponse("Password reset done....")
        
    return render (request, 'app/password_change.html',{'id':id})

# def passwordchangedone(request):
#     if request.method =="POST":
#         id =request.POST['id']
#         password =request.POST['password1']
#         password2= request.POST['password2']
#         user = User.objects.get(id= id)
#         print(user)
#         user.password1 =password
#         user.password2 =password2
#         user.save()
#         return redirect('sign_in')
#     return HttpResponse ("hello")
    # return redirect(request, 'app/sign_in.html')


def passwordchangedone(request):
    if request.method =="POST":
        id =request.POST['id']
        password =request.POST['password']
        password2= request.POST['password1']
        user = User.objects.get(id= id)
        if password == password2:
            user.set_password(password)
            user.save()        
            return redirect('sign_in')
    return render(request,'app/password_change.html')


def contact(request):
    if request.method =="POST":
        fname =request.POST['fname']
        email=request.POST['email']
        message=request.POST['message']

        
        contact_info= Contact(name=fname,
                              email=email,
                              message=message)
        messages.success(request, "Contact Sucessfull")
        contact_info.save()
        subject="contact info"
        message=f"Thank you for contacting us"
        email_from= settings.EMAIL_HOST_USER
        recipient_list= [email]
        send_mail(subject,message,email_from,recipient_list)
     
    return render(request,'app/contact.html')
