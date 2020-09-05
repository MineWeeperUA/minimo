# Generated by Django 3.1 on 2020-08-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200816_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_image',
            field=models.ImageField(default=None, upload_to='title_images', verbose_name='Титульне зображення'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='Кількість дизлайків'),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Кількість лайків'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='Кількість дизлайків'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Кількість лайків'),
        ),
    ]
