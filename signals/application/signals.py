from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from .tasks import send_post_email_task, send_post_deleted_email

# Post Created
@receiver(post_save, sender=Post)
def send_post_created_email(sender, instance, created, **kwargs):
    if created:
        send_post_email_task.delay(instance.user.username, instance.user.email, instance.title, instance.content)

# Post Deleted
@receiver(post_delete, sender=Post)
def send_post_deleted_email_signal(sender, instance, **kwargs):
    send_post_deleted_email.delay(instance.user.username, instance.user.email, instance.title, instance.content)

