from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    date = models.DateField()
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    img_url = models.ImageField()

    def __str__(self):
        return self.name