from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.title
