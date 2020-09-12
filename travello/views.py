from django.http import HttpResponse
from django.shortcuts import render

from .models import places

# Create your views here.


def index(request):
    # dest1 = places()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'Mumbai is the city of bollywood'
    # dest1.price = 1000
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = True

    dests = places.objects.all()

    return render(request, 'index.html', {'dests': dests})
