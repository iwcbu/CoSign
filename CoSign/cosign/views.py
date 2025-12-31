# cosign/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import models
from django.views.generic import View, ListView, DetailView
from .models import *

# Create your views here.

#       Views are the foundational components that structure
#   the project's user experience logic. These control what the 
#   user



# =============================================
#       Temporary View for easy access to 
#       setup and test views
#
#           - ShowAllProfiles
#
# =============================================

class ShowAllProfiles(ListView):

    model = Profile
    template_name = 'cosign/show_all_profiles.html'
    context_object_name = 'profiles'



# =============================================
#                  Profile
#
#           - ProfileDetailView
#           - ProfileCreateView
#           - ProfileUpdateView
#           - ProfileDeleteView
#           - ShowFollowersDetailView
#           - ShowFollowingDetailView
#
# =============================================

class ProfileDetailView(DetailView):
    '''Class definition for Profile page'''

    model = Profile
    template_name = 'cosign/profile/show_profile.html'

    def get_context_data(self, **kwargs):
        '''Gets context data for a page'''

        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context['profile'] = profile

        return context




# =============================================
#                   Feed
#
#           - CoSignFeedView
#           - PrivateFeedView
#           - SearchView
#
# =============================================



# =============================================
#                   Post
#
#           - PostDetailView
#           - PostCreateView
#           - PostUpdateView
#           - PostDeleteView
#
# =============================================






# =============================================
#               Interactions
#           
#           - CosignView
#           - LikeView
#           - FollowView
# 
# =============================================




