from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    autor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comment(models.Model):
    post = models.CharField(verbose_name='Тема письма*', max_length=80)
    email = models.EmailField(verbose_name='Ваша почта*')
    body = models.TextField(verbose_name='Текст сообщения')
    date = models.DateTimeField('Дата', default=timezone.now)

    def get_absolute_url(self):
        return reverse('comment-view')

    def __str__(self):
        return f'{self.post}'

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментов'
