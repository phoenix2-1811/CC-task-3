from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('uploadfile/', uploadapi.as_view() ),
    path('getfile/<str:filename>/',retrievedata.as_view()),
    path('rmfile/<str:filename>/',removefile.as_view())
]