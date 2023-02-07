from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)

class Another(models.Model):
    name = models.CharField(max_length=100)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

class Some(models.Model):
    some = models.CharField(max_length=100)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)


class Brand(models.Model):
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class Inventory(models.Model):
    inventory = models.CharField(max_length=100)
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
