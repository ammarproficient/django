from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='Post', null=True, blank=True)

    def __str__(self):
        return self.title
