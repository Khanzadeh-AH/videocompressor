from .models import Video
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import compress_video


@receiver(post_save, sender=Video)
def compress(sender, instance, **kwargs):
    compress_video.delay(instance.id)
