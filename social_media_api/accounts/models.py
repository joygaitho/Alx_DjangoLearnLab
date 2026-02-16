from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Unique name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Unique name
        blank=True
    )

    def __str__(self):
        return self.username
    