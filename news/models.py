from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    announce = models.CharField(max_length=250, verbose_name='Анонс')
    full_text = models.TextField(verbose_name='Статья')
    date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
