from django.db import models

# Create your models here.


class table_yy(models.Model):

    username = models.CharField(max_length=50)
    passward = models.CharField(max_length=50)