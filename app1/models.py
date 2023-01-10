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


class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
