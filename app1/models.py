from django.db import models


class Paragraph(models.Model):
    title = models.CharField('Заголовок', max_length=50, blank=True, null=True)
    text = models.TextField('Текст')
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы на Главной'


class DemandPage(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Страница "Востребованность"'

