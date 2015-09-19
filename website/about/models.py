from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()
    parent = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.title
