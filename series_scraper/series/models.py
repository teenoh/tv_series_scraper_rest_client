from django.db import models

# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Seasons(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField
    series = models.ForeignKey(Series, on_delete=models.Cascade)

    def __str__(self):
        return self.name

class Episodes(models.Model):
    name = models.CharField(max_length=20)
    download_link = models.URLField()

