# cosign/views.py

from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

#       Views are the foundational components that structure
#   the project's user experience logic. These control what the 
#   user

class HomeView(TemplateView):
    
    template_name = 'cosign/home/home.html'

class ProfileDetailView(TemplateView):

    template_name = 'cosign/profile/show_profile.html'
