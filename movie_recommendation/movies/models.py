from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.FloatField()

    def __str__(self):
        return self.name

