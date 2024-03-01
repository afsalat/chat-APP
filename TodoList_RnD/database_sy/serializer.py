from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):

    class Meta: 
        model = table_yy
        fields = ['username','passward',]