# Generated by Django 4.1.3 on 2022-11-26 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_alter_readlater_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.URLField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('name', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
