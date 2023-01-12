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


class AnalyticsByYear(models.Model):
    year = models.IntegerField('Год')
    average_salary = models.IntegerField('Средняя З/П')
    average_salary_web = models.IntegerField('Средняя З/П - Web-разработчик')
    vacancies = models.IntegerField('Количество вакансий')
    vacancies_web = models.IntegerField('Количество вакансий - Web-разработчик')

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class GeographyPage(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Страница "География"'


class SalaryByCity(models.Model):
    city = models.CharField('Город', max_length=25)
    average_salary = models.IntegerField('Средняя З/П, руб')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города - З/П'


class VacanciesByCity(models.Model):
    city = models.CharField('Город', max_length=25)
    vacancies = models.FloatField('Доля вакансий, %')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города - Доля вакансий'