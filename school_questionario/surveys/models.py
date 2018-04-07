from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.SlugField(max_length=64, primary_key=True)

    def __str__(self):
        return self.name
