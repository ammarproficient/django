from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import Profile, Post

User = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Pehle default User admin ko unregister karo
admin.site.unregister(User)
# Ab custom UserAdmin register karo
admin.site.register(User, UserAdmin)
admin.site.register(Post)