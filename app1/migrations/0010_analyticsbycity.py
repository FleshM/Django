# Generated by Django 4.1.4 on 2023-01-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_geographypage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsByCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25, verbose_name='Город')),
                ('average_salary', models.IntegerField(verbose_name='Средняя З/П, руб')),
                ('vacancies', models.FloatField(verbose_name='Доля вакансий, %')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
