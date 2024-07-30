from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10)

    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# python managee.py shell
"""
 1.增
 Book.objects.create(
     name = '1'
 )
"""

"""
2.查询
Book.objects.get(1)
Book.objects.all()
"""
