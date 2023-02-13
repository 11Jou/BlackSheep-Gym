from django.db import models

class Account(models.Model):
    Name = models.CharField(max_length=50)
    Mail = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name