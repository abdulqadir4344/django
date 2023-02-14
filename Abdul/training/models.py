from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    phone = models.IntegerField(max_length=11)
    address = models.CharField(max_length=80)
    desc = models.CharField(max_length=80)
    date = models.DateField()

    def __str__(self):
        return self.name
    




