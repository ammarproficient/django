from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile, Post

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='profile.bio', required=False, allow_blank=True)
    confirm_password = serializers.CharField(write_only=True, required=False)
    display_picture = serializers.ImageField(source='profile.display_picture', required=False, allow_null=True)
    remove_image = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'password', 'confirm_password', 'display_picture', 'remove_image']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}


    def validate(self, attrs):
        if self.instance is None:
            if attrs.get('password') != attrs.get('confirm_password'):
                raise serializers.ValidationError("Passwords do not match")

        return attrs


    def validate_username(self, value):
        user = self.instance
        if user:  # update case
            if User.objects.exclude(id=user.id).filter(username=value).exists():
                raise serializers.ValidationError("This username is already taken")
        else:  # create case
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("This username is already taken")

        return value


    def validate_email(self, value):
        user = self.instance
        if user:  # update case
            if User.objects.exclude(id=user.id).filter(email=value).exists():
                raise serializers.ValidationError("This email is already in use")
        else:  # create case
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("This email is already in use")

        return value

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        profile_data = validated_data.pop('profile', {})
        display_picture = profile_data.get('display_picture')

        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user)

        if display_picture:
            profile.display_picture = display_picture
            profile.save()

        return user

    def update(self, instance, validated_data):
        validated_data.pop('confirm_password', None)
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password', None)
        remove_image = validated_data.pop('remove_image', False)

        # Update user fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()

        # Update profile image
        profile = instance.profile

        if 'bio' in profile_data:
            profile.bio = profile_data['bio']

        if remove_image:
            profile.display_picture.delete(save=False)
            profile.display_picture = None
        elif 'display_picture' in profile_data:
            profile.display_picture = profile_data['display_picture']

        profile.save()
        return instance



class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # username return karega
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)  # user ka id bhi return karega
    # create/update ke liye user hidden field rakhenge
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ["id", "user", "user_id", "title", "description", "image", "created_at", "updated_at", "created_by"]
        extra_kwargs = {
            "created_by": {"write_only": True},
        }

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long")
        return value

    # Explicit create
    def create(self, validated_data):
        validated_data["user"] = validated_data.pop("created_by")
        return Post.objects.create(**validated_data)

    # Explicit update
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        if "image" in validated_data:
            instance.image = validated_data["image"]
        instance.save()
        return instance
