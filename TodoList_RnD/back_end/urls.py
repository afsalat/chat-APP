from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from database_sy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', table_yy.as_view(), name="some")
]
