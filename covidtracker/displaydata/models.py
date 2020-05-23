from django.db import models



class Summary(models.Model):
    country = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    slug = models.CharField(max_length=50)
    new_confirmed = models.IntegerField()
    total_confirmed = models.IntegerField()
    new_deaths = models.IntegerField()
    total_deaths = models.IntegerField()
    new_recovered = models.IntegerField()
    total_recovered = models.IntegerField()
    date = models.DateTimeField()


class WorldTotal(models.Model):
    total_confirmed = models.IntegerField()
    total_deaths = models.IntegerField()
    total_recovered = models.IntegerField()
