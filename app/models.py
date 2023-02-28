from django.db import models


class DefaultColumnValues():
    def actions_default():
        return ['R']


""" https://docs.djangoproject.com/en/4.1/ref/models/fields/ """
class ProfileModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    """ https://docs.djangoproject.com/en/4.1/ref/models/options/ """
    class Meta:
        db_table = "profile"


class PermissionModel(models.Model):
    resource = models.CharField(max_length=100, blank=False)
    """ https://realpython.com/python-lambda/  """
    actions = models.JSONField("actions", default=DefaultColumnValues.actions_default)
    profile = models.ForeignKey(ProfileModel, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "permission"
        unique_together = ['profile', 'resource']


class UserModel(models.Model):
    name = models.CharField(max_length=100, blank=False),
    email = models.CharField(unique=True, max_length=150, blank=False),
    password = models.CharField(max_length=100)
    profile = models.ForeignKey(ProfileModel, blank=False, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name
