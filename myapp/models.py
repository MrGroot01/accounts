from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)   # ✅ NEW
    picture = models.URLField(null=True, blank=True)   

    def __str__(self):
        return self.name


class LoginHistory(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    login_date = models.DateField(auto_now_add=True)
    login_time = models.TimeField(auto_now_add=True)
    login_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.login_datetime}"