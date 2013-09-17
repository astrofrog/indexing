from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from main.models import Quantity, QuantityDefinition

from datetime import datetime


def add_quantity(request):

    # First retrieve all the required arguments

    try:
        name = request.POST['name']
    except:
        return HttpResponse("name is missing")

    try:
        object = request.POST['object']
    except:
        return HttpResponse("object is missing")

    try:
        value = float(request.POST['value'])
    except:
        return HttpResponse("value is missing")

    try:
        unit = float(request.POST['unit'])
    except:
        return HttpResponse("unit is missing")

    try:
        user = request.POST['user']
    except:
        return HttpResponse("user is missing")

    # Instantiate the quantity

    q = Quantity(definition=name,
                 object=object,
                 value=value,
                 unit=unit,
                 user=user,
                 date_entered=datetime.now()
                 )

    # Now optionally set the remaining properties

    if 'uncertainty' in request.POST:
        q.uncertainty = float(request.POST['uncertainty'])

    if 'origin' in request.POST:
        q.origin = request.POST['origin']

    return HttpResponse("success")
