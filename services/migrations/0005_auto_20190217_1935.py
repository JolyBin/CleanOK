# Generated by Django 2.0.4 on 2019-02-17 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20190217_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.Category', verbose_name='Категория услуги'),
        ),
    ]
