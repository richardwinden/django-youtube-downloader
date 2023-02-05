from pytube import YouTube
from rest_framework import serializers

from download.models import Download


def clean_filename(name):
    """Ensures each file name does not contain forbidden characters and is within the character limit"""

    forbidden_chars = '"*\\/\'.|?:<>,'
    filename = (''.join([x if x not in forbidden_chars else '' for x in name])).replace('  ', ' ').strip()
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename


class VideoSerializer(serializers.Serializer):
    def __init__(self, **kwargs):
        video = YouTube(f"https://www.youtube.com/watch?v={kwargs['data']['code']}")
        kwargs["data"]["title"] = video.title
        kwargs["data"]["thumbnail_url"] = video.thumbnail_url
        kwargs["data"]["author"] = video.author
        kwargs["data"]["watch_url"] = video.watch_url
        kwargs["data"]["filename"] = clean_filename(video.title) + ".mp4"
        download = Download.objects.create()
        kwargs["data"]["download_id"] = download.id
        super().__init__(**kwargs)

    code = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    thumbnail_url = serializers.URLField(required=True)
    author = serializers.CharField(required=True)
    watch_url = serializers.URLField(required=True)
    filename = serializers.CharField(required=True)
    download_id = serializers.IntegerField(required=True)
