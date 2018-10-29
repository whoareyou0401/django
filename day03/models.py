from django.db import models

# Create your models here.
class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    age = models.IntegerField(
        default=1
    )

    money = models.IntegerField(
        default=0
    )

class IdCard(models.Model):
    num = models.CharField(
        max_length=20,
        verbose_name='身份证号'
    )
    addre = models.CharField(
        max_length=50,
        verbose_name='河南'
    )
    class Meta:
        verbose_name = '身份证类'

class Person(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='姓名'
    )
    idcard = models.OneToOneField(IdCard)

    def __str__(self):
        return self.name


class Classes(models.Model):
    cname = models.CharField(max_length=20)

    def __str__(self):
        return self.cname

class Student(models.Model):
    s_name = models.CharField(max_length=30)
    classes = models.ForeignKey(Classes)

    def __str__(self):
        return self.s_name



class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)

    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.name

class HumenBase(models.Model):
    name = models.CharField(max_length=30)

    age = models.IntegerField()

    sex = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Teacher(HumenBase):
    t_no = models.CharField(max_length=20)

class Schooer(HumenBase):
    hobby = models.CharField(max_length=200)

















