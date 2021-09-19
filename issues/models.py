from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Issue(models.Model):
    CATEGORY_CHOICES = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3')
    )

    title = models.CharField(max_length=50)

    resolved = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    developer = models.ForeignKey("Developer", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} | {self.developer} | resolved: {self.resolved}"

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email