from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from main.models import Quantity, QuantityDefinition

from datetime import datetime

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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
    except KeyError:
        return HttpResponse("value is missing")
    except ValueError:
        return HttpResponse("value should be a float")
        
    try:
        unit = request.POST['unit']
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

    # Save quantity to database
    q.save()

    return HttpResponse("success")
