from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255, null=False)
    original_video = models.FileField(upload_to='', null=False, verbose_name='Original Video')
    video_240 = models.FileField(upload_to='video240', null=True, verbose_name='Video 240', blank=True)
    video_360 = models.FileField(upload_to='video360', null=True, verbose_name='Video 360', blank=True)
    took_time = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.name
