from django.contrib import admin
from .models import UserRegister, LoginHistory

admin.site.register(UserRegister)
admin.site.register(LoginHistory)