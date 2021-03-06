# Generated by Django 3.1 on 2020-08-19 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200819_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.language'),
        ),
    ]
