# Generated by Django 4.1 on 2022-08-31 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': [('view_not_moderated_review', 'Видеть немодерированные отзывы')], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
