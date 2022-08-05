import os
import time
import subprocess
from celery import shared_task
from .models import Video
from django.conf import settings
from datetime import timedelta
from django.core.files import File
from pathlib import Path

MEDIA_ROOT = settings.MEDIA_ROOT
v240_path = os.path.join(MEDIA_ROOT, 'video240')
v360_path = os.path.join(MEDIA_ROOT, 'video360')


@shared_task
def compress_video(video_id):
    video = Video.objects.filter(id=video_id).first()
    if (not video.video_240) or not video.video_360:
        # video_path = os.path.join(MEDIA_ROOT, str(video.original_video))
        video_path = video.original_video.path
        start_time = time.time()
        p = subprocess.Popen(
            f'ffmpeg -i {video_path} -threads 0 -preset ultrafast -s 640x360 -c:v libx264 {v360_path}/{str(video.original_video)} -threads 0 -preset ultrafast -s 320x240 -c:v libx264  {v240_path}/{str(video.original_video)}',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        video.video_240.name = f'{v240_path}/{str(video.original_video)}'
        video.video_360.name = f'{v360_path}/{str(video.original_video)}'

        end_time = time.time()
        exec_time = end_time - start_time
        video.took_time = timedelta(seconds=exec_time)
        video.save()

    return True
