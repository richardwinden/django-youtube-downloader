from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('youtube/<str:video_code>', download_video_view),
]
