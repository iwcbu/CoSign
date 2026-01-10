# cosign/views.py

from .forms import *
from .models import *

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import \
    View,       \
    ListView,   \
    DetailView, \
    CreateView, \
    UpdateView, \
    DeleteView

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
    



# class ProfileCreateView(CreateView):

#     model = Profile
#     form_class = CreateProfileForm
#     template_name = 'cosign/profile/create_profile'

#     def get_context_data(self, **kwargs):
#         '''provides context data for the create view'''

#         context = super().get_context_data()

#         if self.request.method == 'POST':
#             userForm = UserCreationForm(self.request.POST)
#             profileForm = CreateProfileForm(self.request.POST, self.request.FILES)
#         else:
#             userForm = UserCreationForm()
#             profileForm = CreateProfileForm()
        
#         context['userForm'] = userForm
#         context['profileForm'] = profileForm

#         return context

#     def form_valid(self, form):
#         '''Submits a new profile object to the database given and valid creation form'''

#         userForm = UserCreationForm(self.request.POST)

#         if userForm.is_valid():
#             user = userForm.save()
#             login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
#             form.instance.user = user

#         return super().form_valid(form)
    
#     def get_success_url(self):
#         '''returns ProfileDetailView's after successful profile update'''

#         return reverse("show_profile", kwargs={"pk": self.object.pk})



class ProfileUpdateView(UpdateView):
    '''View that displays the page to update a profile'''


    model = Profile
    form_class = UpdateProfileForm
    template_name = 'cosign/profile/update_profile.html'
    context_object_name = 'profile'

    def get_success_url(self):
        '''returns ProfileDetailView's after successful profile update'''

        return reverse("show_profile", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        '''provides context data for update view'''

        context = super().get_context_data()

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context['profile'] = profile

        return context


#        IMPLEMENT LOGINREQUIREDMIXIN BEFORE DELETE VIEW

# class ProfileDeleteView(DeleteView):

#     model = Profile
#     template_name = 'cosign/profile/update_profile'

    
#     def get_context_data(self, **kwargs):
#         '''provides context data for update view'''

#         context = super().get_context_data()

#         pk = self.kwargs['pk']
#         profile = Profile.objects.get(pk=pk)
#         context['profile'] = profile

#         return context
    
#     def get_success_url(self):
#         '''returns ProfileDetailView's after successful profile update'''

#         return reverse("show_all_profiles")
    
    




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




