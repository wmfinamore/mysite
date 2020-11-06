from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, help_text='blog title')
    slug = models.SlugField(max_length=250, unique_for_date='publish',
                            help_text='short label to be used in URL')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts',
                               help_text='user that wrote the blog')
    body = models.TextField(help_text='body of the blog')
    publish = models.DateTimeField(default=timezone.now,
                                   help_text='when the blog was published')
    created = models.DateTimeField(auto_now_add=True,
                                   help_text='when the blog was created')
    update = models.DateTimeField(auto_now=True, help_text='last time that the blog was updated')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft',
                              help_text='status of a blog')
    objects = models.Manager()#The default manager
    published = PublishedManager()#Our custom manager

    class Meta:
        """sort results by the publish field in descending order by default"""
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.PROTECT,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
