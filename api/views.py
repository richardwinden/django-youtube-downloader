from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import VideoSerializer
from download.models import Download


@api_view(["GET"])
def video_details_view(request):
    print(request.GET)
    video = VideoSerializer(data=request.GET.copy())
    if video.is_valid():
        return Response(video.data)


@api_view(["GET"])
def get_progress_view(request, download_id):
    return Response({"progress": Download.objects.get(id=download_id).progress})
# Create your views here.
