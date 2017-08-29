from django.db import models

# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
 
    def __str__(self):
        return self.name

class Seasons(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(blank = True)
    series = models.ForeignKey(Series, related_name="seasons",  on_delete=models.CASCADE)

    def __str__(self):
        return "{ser}-{sea}".format(ser=self.series, sea=self.name)

class Episodes(models.Model):
    name = models.CharField(max_length=20)
    download_link = models.URLField()
    season = models.ForeignKey(Seasons, related_name="episodes", on_delete=models.CASCADE)

    def __str__(self):
        return "{ser}-{sea}-{epis}".format(ser=self.season.series.name,
                                           sea=self.season.name,
                                           epis=self.name)


