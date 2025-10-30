from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_post_email_task(username, email, title, content):
    subject = f"Your Post '{title}' Has Been Created"
    message = f"Hi {username},\n\nYou have created a new post titled: \"{title}\".\n\nThanks for using our website! {content}"
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [email])


@shared_task
def send_post_deleted_email(username, email, title, content):
    subject = f"Your Post '{title}' Has Been Deleted"
    message = f"Hi {username}, your post titled '{title}' has been deleted. {content}"
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [email])

