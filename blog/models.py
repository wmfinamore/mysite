from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, help_text='post title')
    slug = models.SlugField(max_length=250, unique_for_date='publish',
                            help_text='short label to be used in URL')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts',
                               help_text='user that wrote the post')
    body = models.TextField(help_text='body of the post')
    publish = models.DateTimeField(default=timezone.now,
                                   help_text='when the post was published')
    created = models.DateTimeField(auto_now_add=True,
                                   help_text='when the post was created')
    update = models.DateTimeField(auto_now=True, help_text='last time that the post was updated')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',
                              help_text='status of a post')
    objects = models.Manager()#The default manager
    published = PublishedManager()#Our custom manager

    class Meta:
        """sort results by the publish field in descending order by default"""
        ordering = ('-publish',)

    def __str__(self):
        return self.title


