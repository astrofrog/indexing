from django.db import models

# See https://docs.djangoproject.com/en/dev/ref/models/fields/#datetimefield for a list of field classes.


class QuantityDefinition(models.Model):
    """
    Defines the meaning of a quantity, for use in a Glossary
    """
    name = models.CharField(max_length=100)
    description = models.TextField()


class Quantity(models.Model):
    """
    A 'well defined quantity'
    """
    quantity = models.ForeignKey(QuantityDefinition)
    object_name = models.CharField(max_length=100)
    value = models.FloatField()
    uncertainty = models.FloatField()
    unit = models.CharField(max_length=100)
    origin = models.URLField()
    date = models.DateTimeField()
    date_entered = models.DateTimeField()
    user_entered = models.CharField(max_length=100)


# models.ForeignKey(QuantityDefinition)