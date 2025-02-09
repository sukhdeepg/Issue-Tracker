from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_owner = models.BooleanField(default=True)
    is_developer = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Issue(models.Model):
    CATEGORY_CHOICES = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3')
    )

    title = models.CharField(max_length=50)

    resolved = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    team = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # team in which the developer belongs
    developer = models.ForeignKey("Developer", on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey("Category", related_name="issues", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} | {self.developer} | resolved: {self.resolved}"

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # team in which the developer belongs

    def __str__(self):
        return self.user.email
        
class Category(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)