from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('about', views.about, name= 'about'),
    path('account', views.account, name= 'account'),
    path('contact', views.contact, name= 'contact'),
    path('sport_relatedcategory/<slug:slug>',views.sport_relatedcategory,name='sport_relatedcategory'),
    path('blogs', views.blogs, name='blogs'),
    path('blogdetails/<slug:slug>', views.blogdetails, name= 'blogdetails'),
    path('gallery', views.gallery, name= 'gallery'),
    path('booking', views.booking, name='booking'),
    path('history', views.history, name= 'history'),
    path('atheletes', views.atheletes, name= 'atheletes'),
    path('atheletes_details/<slug:slug>',views.atheletes_details,name='atheletes_details'),
    path('sports', views.sports, name= 'sports'),
    path('sport_details/<slug:slug>',views.sport_details,name='sport_details'),
    path('login', views.login, name= 'login'),
    path('matchresult', views.matchresult, name= 'matchresult'),
    path('leaguestandings', views.leaguestandings, name= 'leaguestandings'),
    path('match_schedule', views.match_schedule, name= 'match_schedule'),
    path('news', views.news, name= 'news'),
    path('logout', views.custom_logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('change-password', views.change_password, name='changepassword'),
    path('password_change', views.password_change,name='password_change'),
    path('reset/password/<uid>/<token>', views.restpasword,name='password_change'),
    path('streaming', views.streaming,name='streaming'),
    path('comments', views.comments,name='comments'),
    path('forgot_password', views.forgot_password,name='forgot_password'),
    # path('password/change/done',views.restpasword,name='password_change_done'),
    path('password/change/success',views.passwordchangedone,name='passwordchangedone')
 
    

    ]+ static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)