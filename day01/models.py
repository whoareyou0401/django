from django.db import models

# Create your models here.
class Humen(models.Model):
    name = models.CharField(
        max_length=30
    )
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):

        return self.name









