from django.urls import path

from database_sy import views

urlpatterns = [
    path('',views.storage, name="info")
]
