from django.db import models


class Ebook(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    cover_url = models.CharField(max_length=2048)

    def __str__(self):
        return self.title


class CartItems(models.Model):
    title = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
