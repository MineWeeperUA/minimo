# Generated by Django 3.1 on 2020-08-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200819_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text_on_main',
            field=models.TextField(default='TEXT ON MAIN', help_text='Введіть текст статті, що відобразиться на головній сторінці', verbose_name='Текст статті на головній сторінці'),
            preserve_default=False,
        ),
    ]
