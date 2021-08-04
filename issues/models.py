from django.db import models

class Issue(models.Model):
    CATEGORY_CHOICES = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3')
    )

    title = models.CharField(max_length=50)

    resolved = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)

    