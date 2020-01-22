import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rooms.models import Room
# Create your views here.

def list_rooms(Request):
    data = serializers.serialize("json", Room.objects.all())
    response = HttpResponse(content=data)
    return response
