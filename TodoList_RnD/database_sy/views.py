# from django.shortcuts import render
from database_sy.models import table_yy
from django.http import JsonResponse

# Create your views here.

def storage(request):
    
    cts = table_yy.objects.all()
    data = [{'username': ct.username, 'passward': ct.passward} for ct in cts]

    return JsonResponse(data, safe=False)
