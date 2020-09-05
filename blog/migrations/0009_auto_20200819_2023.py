# Generated by Django 3.1 on 2020-08-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200819_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.SlugField(default='sample', max_length=130, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(help_text='Оберіть категорію', to='blog.Category'),
        ),
    ]
