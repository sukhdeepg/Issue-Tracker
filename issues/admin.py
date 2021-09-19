from django.contrib import admin

from .models import User, Issue, Developer

admin.site.register(User)
admin.site.register(Issue)
admin.site.register(Developer)