from django.db import models

class Offer(models.Model):
    title = models.CharField(max_length=10, choices=[('3 Month','3 Month Subscription'),('6 Month','6 Month Subscription'),
    ('Year' ,'Year Subscription') , ('Yoga' , 'Yoga Sessions'), ('Boxing', 'Kick Boxing Sessions')], default="String")
    price = models.IntegerField()
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='offers/%y/%m/%d')

    def __str__(self):
        return self.title
