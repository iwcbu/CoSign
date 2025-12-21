# cosign/urls.py

from django.urls import path
from .views import *
from django.views.generic import TemplateView
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
    path('', TemplateView.as_view(), name='home'),
    path('/home', TemplateView.as_view(), name='home'),

    #Feed

    #
]