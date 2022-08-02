from django.shortcuts import render
from django.conf import settings
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    return render(request,'blog/index.html',{})
