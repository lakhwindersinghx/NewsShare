# Generated by Django 4.1.3 on 2022-11-29 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0006_likednews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav1', models.CharField(max_length=300, null=True)),
                ('fav2', models.CharField(max_length=300, null=True)),
                ('fav3', models.CharField(max_length=300, null=True)),
                ('fav4', models.CharField(max_length=300, null=True)),
                ('fav5', models.CharField(max_length=300, null=True)),
                ('name', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]