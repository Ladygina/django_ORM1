from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    image = models.URLField(max_length=150)
    release_date = models.CharField(max_length=150)
    lte_exists = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
