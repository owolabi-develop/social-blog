from django.shortcuts import render
from django.conf import settings
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreationForm
from django.db.models.signals import post_save
from .models import Profile


# Create your views here.
def post_save_Profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(post_save_Profile, sender=settings.AUTH_USER_MODEL)
        

def index(request):
    return render(request,'blog/index.html',{})

def UserLogin(request):
    return render(request,'blog/login.html',{})

def UserSignUp(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
    else:
        form = UserCreationForm()
            
    return render(request,"blog/signup.html",{'form':form})

def Signup_success(request):
    return render(request,'blog/Signup_success.html')

def UserProfile(request):
    return render(request,"blog/profile.html",{})

def details(request,blog_id=1):
    return render(request,"blog/details.html",{})

def forgotPassword(request):
     return render(request,"blog/forgetpassword.html",{})