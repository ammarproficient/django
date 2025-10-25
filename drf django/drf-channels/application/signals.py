from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Task
from .tasks import send_email_task


@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications_group",
            {
                "type": "send_notification",  # ye function consumer me hona chahiye
                "title": instance.title
            }
        )


@receiver(post_save, sender=Task)
def send_notification_task(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "task",
            {
                "type": "send_notification_task",
                "title": instance.title
            }
        )
        # Background Email (after 5 sec)
        send_email_task.delay(instance.title, "receiveremail@example.com")
