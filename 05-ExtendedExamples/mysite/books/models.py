from django.db import models

# Create your models here.

# Table relations;
# ForeignKey = N:1
# ManyToManyField = N:N
# OneToOneField = 1:1
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title
    
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    