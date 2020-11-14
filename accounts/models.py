from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(max_length=50, blank=True)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)
    created_info = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_info = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
        ordering = ['-created_info']