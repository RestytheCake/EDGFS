# Generated by Django 3.2.13 on 2023-02-17 17:27

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
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(blank=True, max_length=255)),
                ('main_post_user', models.CharField(blank=True, max_length=255)),
                ('main_post_title', models.CharField(blank=True, max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, default=',', max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NickUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('discord_member', models.BooleanField(default=False)),
                ('discord_name', models.CharField(blank=True, max_length=255)),
                ('supporter', models.BooleanField(default=False)),
                ('special', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('confirm', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(blank=True, max_length=255)),
                ('Post_title', models.CharField(blank=True, max_length=255)),
                ('Post_message', models.CharField(blank=True, max_length=255)),
                ('Post_Tags', models.CharField(blank=True, max_length=255)),
                ('Warning', models.CharField(blank=True, max_length=255)),
                ('Description', models.CharField(blank=True, max_length=255)),
                ('Sender', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_member', models.BooleanField(default=False)),
                ('discord_name', models.CharField(blank=True, max_length=255)),
                ('special', models.BooleanField(default=False)),
                ('special_roles', models.CharField(blank=True, max_length=255)),
                ('long_supporter', models.BooleanField(default=False)),
                ('muffin_family', models.BooleanField(default=False)),
                ('muffin_role', models.CharField(blank=True, max_length=255)),
                ('fa_list', models.ManyToManyField(blank=True, related_name='fa_list', to=settings.AUTH_USER_MODEL)),
                ('fa_send', models.ManyToManyField(blank=True, related_name='fa_send', to=settings.AUTH_USER_MODEL)),
                ('friend_list', models.ManyToManyField(blank=True, related_name='friend_list', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=' ', max_length=255)),
                ('title', models.CharField(default='', max_length=100)),
                ('message', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dislike', models.ManyToManyField(blank=True, related_name='dislike', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]