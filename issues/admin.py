from django.contrib import admin

from .models import User, Issue, Developer, UserProfile, Category

admin.site.register(User)
admin.site.register(Issue)
admin.site.register(Developer)
admin.site.register(UserProfile)
admin.site.register(Category)