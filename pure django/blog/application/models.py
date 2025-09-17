from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='blog-images/')

    def __str__(self):
        return f"Image for {self.blog.title}"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title if self.title else "Gallery Image"


class Alert(models.Model):
    alert = models.CharField(max_length=200, blank=True, null=True)
    show = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True, unique=True)  # optional clickable link

    def __str__(self):
        return self.alert if self.alert else "No Alert"

