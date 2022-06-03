from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models.user.models import User


class CustomUserAdmin(UserAdmin):
    model = User


admin.site.register(User, UserAdmin)

