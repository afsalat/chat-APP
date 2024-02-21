from django.shortcuts import render

from database_sy.models import table_yy

# Create your views here.

def storage(request):

    du_data = table_yy.objects.all()

    for x in du_data:
        data = x.username
        return render(request, 'index.html',{'data':data})


    return render(request, 'index.html')