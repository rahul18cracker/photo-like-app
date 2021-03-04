from django.db import models


# Create your models here.
class Product(models.Model):
    """
    Class defines the fields that show up in the UI for each product. Each product can be
    viewed and then liked
    """
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    """
    Will be used to store the user id which is id by default here
    """
    pass
