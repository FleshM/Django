# Generated by Django 4.1.4 on 2023-01-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_years_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Параграф',
                'verbose_name_plural': 'Страница "Навыки"',
            },
        ),
    ]
