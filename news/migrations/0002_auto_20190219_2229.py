# Generated by Django 2.0.4 on 2019-02-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Заголовок'),
        ),
    ]
