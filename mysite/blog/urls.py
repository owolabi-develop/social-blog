from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name ='blog'
urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.UserLogin,name="Login"),
    path("SignUp/",views.UserSignUp,name="SignUp"),
    path("forgotpassword/",views.forgotPassword,name='forgotpassword'),
    path("Signup_success/",views.Signup_success,name='Signup_success'),
    path("Setting/Profile/",views.UserProfile,name="Profile"),
    path("Details/<int:blog_id>/",views.details,name='details')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
