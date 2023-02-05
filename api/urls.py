from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('video/', video_details_view),
    path('get-progress/<str:download_id>', get_progress_view),
]
