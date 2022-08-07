
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from . forms import UserCreationForm, UserPasswordResetForm,UserSetPassword
from . models import Profile,User
from django.contrib.auth.tokens import PasswordResetTokenGenerator as default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_str,force_bytes
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from . tokens import account_activation_token
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetCompleteView



# Create your views here.
def post_save_Profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.get_or_create(User=instance)
post_save.connect(post_save_Profile, sender=settings.AUTH_USER_MODEL)
        

def index(request):
    return render(request,'blog/index.html',{})

def UserLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("blog:Profile",args=(user.get_username(),)))
        else:
             messages.error(request,'Email or Password is incorrect try again')

    return render(request,'blog/login.html')


def UserSignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject_email = "Activate Your Email"
            message = render_to_string('blog/email_template.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':account_activation_token.make_token(user),
                'protocol':'http',
            })
            to_email = form.cleaned_data['email']
            msg = EmailMessage(subject_email,message,to=[to_email])
            msg.content_subtype ="html"
            msg.send()
            return HttpResponseRedirect(reverse("blog:Signup_success"))
    else:
        form = UserCreationForm() 
    return render(request,"blog/signup.html",{'form':form})

class password_reset(PasswordResetConfirmView):
    template_name = "blog/UserSetpassword.html"
    success_url = reverse_lazy("blog:password_reset_complete")


def password_reset_complete(request):
    return render(request,'blog/passwordchange.html')
     
        

def email_confirm(request,uidb64,token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(get_user_model(),pk=uid)
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        return HttpResponseRedirect(reverse("blog:Profile"))
    else:
        return HttpResponse("Activation link invalid")

def Signup_success(request):
    return render(request,'blog/Signup_success.html')

def UserProfile(request,email):
    user = get_object_or_404(get_user_model(),email=email)

    return render(request,"blog/profile.html",{'user':user})

def details(request,blog_id=1):
    return render(request,"blog/details.html",{})

def forgotPassword(request):
    if request.method =="POST":
        form =UserPasswordResetForm(data=request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['email']
            form.save(get_current_site(request),email_template_name='blog/pwd_email_reset.html')
            return HttpResponseRedirect(reverse("blog:password-down"))
    else:
        form = UserPasswordResetForm()

    return render(request,"blog/forgetpassword.html",{"form":form})

def User_logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse("blog:Login"))

def password_down(request):
    return render(request,'blog/password-down.html')