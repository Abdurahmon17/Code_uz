from django.urls import path
from .views import *

urlpatterns = [
    path ('', main, name='Home'),
    path('project/', project, name='Project'),
    ]