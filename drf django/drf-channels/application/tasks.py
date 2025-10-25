from celery import shared_task
from django.core.mail import send_mail
import time

@shared_task
def send_email_task(title, to_email):
    time.sleep(3)  # delay 5 seconds
    send_mail(
        subject=f"New Task Created: {title}",
        message=f"A new task has been created:\n\n{title}",
        from_email="youremail@example.com",
        recipient_list=[to_email],
        fail_silently=False,
    )

# Run the below command to check the logs of celery
# celery -A project_name worker --loglevel=info --pool=solo

# Run the below command for project
# daphne project_name.asgi:application
