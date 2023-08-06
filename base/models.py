from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos/', null=True)

    def __str__(self):
        return self.name
