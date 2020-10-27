# Generated by Django 3.0.10 on 2020-10-22 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='blog title', max_length=250)),
                ('slug', models.SlugField(help_text='short label to be used in URL', max_length=250, unique_for_date='publish')),
                ('body', models.TextField(help_text='body of the blog')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, help_text='when the blog was published')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='when the blog was created')),
                ('update', models.DateTimeField(auto_now=True, help_text='last time that the blog was updated')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', help_text='status of a blog', max_length=10)),
                ('author', models.ForeignKey(help_text='user that wrote the blog', on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
