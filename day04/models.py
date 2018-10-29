from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(
        max_length=30
    )
    desc = models.CharField(
        max_length=100
    )
    def __str__(self):
        return self.name


    def get_desc(self):
        return 'django学习：%s' % self.desc
