# Generated by Django 4.0.1 on 2022-01-16 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
