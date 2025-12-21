# cosign/urls.py

from django.urls import path
from .views import *
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views # generic view for auth


#       urlpatterns is an array or path functions that
#   contain all url destinations within the cosign
#   application

#           path('url', ViewComponent, name='name')

#       The first parameter in the path function is the url
#   pattern, this is what you put in the url after the project
#   domain (e.g. cosign/url). The second parameter is a view components,
#   which is a component that contains the logic to display the html and required
#   context for the page. The last parameter is the name which like a nickname that
#   represents the url pattern in the rest of the django project.

urlpatterns = [

    # Home
    path('', RedirectView.as_view(url="home", permanent=False), name='home'), # redirects a user to CoSign's home page url pattern
    path('home', HomeView.as_view(), name='home'),
    path('profile', ProfileDetailView.as_view(), name='show_profile'),


    #Feed

    #
]