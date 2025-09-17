from django.contrib import admin
from .models import Blog, BlogImage, Alert, GalleryImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('alert', 'show')
    list_editable = ('show',)


@admin.register(GalleryImage)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_editable = ('image',)
