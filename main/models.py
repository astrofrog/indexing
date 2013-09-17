from django.db import models


# See:
# https://docs.djangoproject.com/en/dev/ref/models/fields/#datetimefield
# for a list of field classes.


class QuantityDefinition(models.Model):
    """
    Defines the meaning of a quantity, for use in a Glossary
    """
    name = models.CharField(max_length=100)
    description = models.TextField()


class User(models.Model):
    """
    Define a user
    """
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    date_joined = models.DateTimeField()


class Object(models.Model):
    """
    Define an Astronomical object
    """
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100, blank=True)


class Quantity(models.Model):
    """
    A 'well defined quantity'
    """
    quantity = models.ForeignKey(QuantityDefinition)
    object = models.ForeignKey(Object)
    value = models.FloatField()
    uncertainty = models.FloatField(blank=True)
    unit = models.CharField(max_length=100, blank=True)
    origin = models.URLField(blank=True)
    date = models.DateTimeField(blank=True)
    date_entered = models.DateTimeField()
    user = models.ForeignKey(User)


