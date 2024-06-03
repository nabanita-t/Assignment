# Generated by Django 5.0.6 on 2024-06-03 14:57

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token_version', models.IntegerField(default=1, editable=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserSessionInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('evice_token', models.TextField(null=True)),
                ('device_type', models.CharField(choices=[('WEB', 'WEB'), ('MOBILE', 'MOBILE'), ('IOS', 'IOS')], max_length=100, null=True)),
                ('is_safari', models.BooleanField(default=False)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Session Info',
                'verbose_name_plural': 'User Session Info',
                'ordering': ['-created_at'],
            },
        ),
    ]