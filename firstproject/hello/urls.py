from django.urls import path
from . import views

#whenever a request is sent to this route 'hello/', it will send the request to views.index to handle
urlpatterns = [
    path('', views.index, name='index' )
]