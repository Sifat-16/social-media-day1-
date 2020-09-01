from django.urls import path
from .views import *

urlpatterns = [
    path('myprofile', mytimeline, name="my-time-line"),
    path('myabout', myabout, name="about"),
    path('update', updateprofile, name="myupdate")
]