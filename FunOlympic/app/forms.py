from django import forms 
from django .forms import ModelForm
from captcha.fields import ReCaptchaField
from .models import Contact


# class ContactForm(ModelForm):
#     name = forms.CharField(max_length=50)
#     email=forms.EmailField()
#     message = forms.Textarea()


#     class Meta:
#         model= Contact
#         fields= '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'

class ValidateForm(forms.Form):
    captcha = ReCaptchaField()
