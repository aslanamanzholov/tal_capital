from django.db import models
from django.conf import settings


class Post(models.Model):
    text = models.CharField(max_length=250, verbose_name='Текст')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.text, self.user)
