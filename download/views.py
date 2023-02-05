from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import string
import random
from pytube import YouTube

from download.models import Download




def clean_filename(name):
    """Ensures each file name does not contain forbidden characters and is within the character limit"""

    forbidden_chars = '"*\\/\'.|?:<>,'
    filename = (''.join([x if x not in forbidden_chars else '' for x in name])).replace('  ', ' ').strip()
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename


def download_video_view(request, video_code):
    def progress_function(stream, chunk, bytes_remaining):
        d = Download.objects.get(id=int(request.GET.get("download")), )

        size = stream.filesize
        p = ((size - float(bytes_remaining)) / float(size)) * float(100)
        d.progress = p
        d.save()

    video = YouTube(f"https://www.youtube.com/watch?v={video_code}", on_progress_callback=progress_function)
    stream = video.streams.get_highest_resolution()
    download = stream.download(skip_existing=False, )
    response = HttpResponse(open(download, 'rb'), content_type="video/mp4")
    d = Download.objects.get(id=int(request.GET.get("download")), )

    d.delete()
    print(f"{clean_filename(video.title)}.mp4")
    response['Content-Disposition'] = f'attachment; filename="{clean_filename(video.title)}.mp4"'
    return response
