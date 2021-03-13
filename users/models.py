from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        'Фото пользователя',
        default='default.png',
        upload_to='user_images'
        )

    u_sex = models.CharField(
        'Выберите пол',
        max_length=1,
        default='',
        choices=(
                ('0', ''),
                ('1', 'Мужской'),
                ('2', 'Женский'),
            )
        )
    # mailcheck = models.BooleanField(
    #     'Соглашение про почту',
    #     max_length=1,
    #     # default='',
    #     choices=(
    #             ('0', 'Yes'),
    #             ('2', 'NO'),
    #             )
    #     )

    # u_date = models.DateField(
    #     'Укажите дату рождения'
    # )

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args,**kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
