from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from main.models import Quantity, QuantityDefinition, Object, User

from datetime import datetime

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_quantity(request):

    # First retrieve all the required arguments

    try:
        quantity_name = request.POST['name']
    except:
        return HttpResponse("name is missing")
    else:
        try:
            definition = QuantityDefinition.objects.get(name=quantity_name)
        except ObjectDoesNotExist:
            definition = QuantityDefinition(name=quantity_name)
            definition.save()

    try:
        object_name = request.POST['object']
    except:
        return HttpResponse("object is missing")
    else:
        try:
            object = Object.objects.get(name=object_name)
        except ObjectDoesNotExist:
            object = Object(name=object_name)
            object.save()

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
        user_name = request.POST['user']
    except:
        return HttpResponse("user is missing")
    else:
        try:
            user = User.objects.get(name=user_name)
        except ObjectDoesNotExist:
            user = User(name=user_name)
            user.save()

    # Instantiate the quantity

    q = Quantity(definition=definition,
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
