from django.urls import include,path,re_path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
app_name ='blog'
urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.UserLogin,name="Login"),
    path("SignUp/",views.UserSignUp,name="SignUp"),
    re_path('^Email-Activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z_\-]+)$',
        views.email_confirm, name='Email-activate'),
    path("forgotpassword/",views.forgotPassword,name='forgotpassword'),
    path("Signup_success/",views.Signup_success,name='Signup_success'),
    path("Setting/Profile/<username>/",views.UserProfile,name="Profile"),
    path("Details/<int:blog_id>/",views.details,name='details'),
    path("Logout/",views.User_logOut,name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
