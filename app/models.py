from django.db import models


class ProfileModel(models.Model):
    name = models.CharField(max_length=100, blank=False)


class PermissionModel():
    resource = models.CharField(max_length=100, blank=False)


class UserModel(models.Model):
    name = models.CharField(max_length=100, blank=False),
    email = models.CharField(max_length=150, blank=False),
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
