from django.db import models

# Create your models here.
class Classes(models.Model):
    name = models.CharField(
        max_length=30,
        null=True,
        unique=True
    )
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=30,unique=True)

    age = models.IntegerField()

    classes = models.ForeignKey(Classes)

    def __str__(self):
        return self.name
