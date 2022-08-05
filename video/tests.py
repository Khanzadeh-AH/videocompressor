from django.test import TestCase
from redis import Redis
import subprocess
from .models import Video
from django.conf import settings
from .tasks import compress_video


class Testffmpeg(TestCase):
    def test_ffmpeg_existence(self):
        process = subprocess.Popen(
            'which ffmpeg',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        stderr = process.stderr.read()

        if stderr:
            raise Exception('ffmpeg command not found!')


class TestCompressUpload(TestCase):
    def setUp(self):
        media_root = settings.MEDIA_ROOT
        process = subprocess.Popen(
            f'ffmpeg -y -f lavfi -i testsrc=size=1920x1080:rate=1 -vf hue=s=0 -vcodec libx264 -preset superfast -tune zerolatency -pix_fmt yuv420p -t 1000 -movflags +faststart {media_root}test.mp4',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

    def test_upload(self):
        media_root = settings.MEDIA_ROOT
        test_video = Video(
            name='test video'
        )
        test_video.original_video.name = f'{media_root}/test.mp4'
        test_video.save()

        compress_video(test_video.id)


class TestRedis(TestCase):
    def test_redis_status(self):
        r = Redis(
            host='127.0.0.0',
            socket_connect_timeout=1
        )
        r.ping()
