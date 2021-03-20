from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(default="Коротка ссылка")
    long_link = models.CharField(max_length=255, default="Длинная ссылка")
    title = models.CharField(max_length=150, default="Описание")

    def __str__(self):
        return f'Профайл пользователя {self.user}'

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
