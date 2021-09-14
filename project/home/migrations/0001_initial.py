# Generated by Django 3.2.7 on 2021-09-14 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='user/Pic')),
                ('id_proof', models.FileField(blank=True, null=True, upload_to='user/idProof')),
                ('gender', models.CharField(default='NULL', max_length=8)),
                ('default_password', models.CharField(default='NULL', max_length=9)),
                ('bio', models.TextField(blank=True)),
                ('phNo', models.CharField(max_length=20)),
                ('status', models.CharField(default='NULL', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]