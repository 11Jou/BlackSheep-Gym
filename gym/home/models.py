from django.db import models

class Msg(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Coach(models.Model):
    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=20)
    image = models.ImageField(upload_to='coach/%y/%m/%d')


    def __str__(self):
        return self.Name