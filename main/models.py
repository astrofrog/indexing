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
    coordinates = models.CharField(max_length=100, null=True)


class Quantity(models.Model):
    """
    A 'well defined quantity'
    """
    # definition = models.ForeignKey(QuantityDefinition)
    # object = models.ForeignKey(Object)
    definition = models.CharField(max_length=100)
    object = models.CharField(max_length=100)
    value = models.FloatField()
    uncertainty = models.FloatField(null=True)
    unit = models.CharField(max_length=100, null=True)
    origin = models.URLField(null=True)
    date = models.DateTimeField(null=True)
    date_entered = models.DateTimeField()
    # user = models.ForeignKey(User)
    user = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "Quantity '" + self.definition + "' for object '" + self.object + "'"


