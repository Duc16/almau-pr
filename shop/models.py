from django.db import models

class Product(models.Model):
    name = models.CharField(null=False, default='', max_length=100)
    descriptions = models.TextField(null=False, default='', max_length=1000)
    price = models.IntegerField(null=False, default=0)
    amount = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'ID: {self.id} {self.name}'

