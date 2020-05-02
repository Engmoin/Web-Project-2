# Generated by Django 3.0.3 on 2020-04-30 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20200424_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('present_address', models.TextField()),
                ('perment_address', models.TextField()),
                ('bio', models.TextField()),
                ('birthday', models.DateField(blank=True, null=True)),
                ('contact', models.TextField(max_length=13)),
            ],
        ),
        
    ]
