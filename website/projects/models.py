from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumbnail = models.ForeignKey('Picture', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Picture(models.Model):
    address = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    matching_post = models.ForeignKey('Post', null=True, blank=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Link(models.Model):
    address = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    matching_post = models.ForeignKey('Post', null=True, blank=True)

    def __str__(self):
        return self.title
