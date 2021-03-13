from django.contrib import admin
from .models import Profile # 1.1 Регистрируем если зайдем в панель админа на сайт все показывает
# Чтобы не захламлять рисунками переходим 1.2 setting.py

# Register your models here.

admin.site.register(Profile)
