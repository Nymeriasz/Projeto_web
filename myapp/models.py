from django.db import models
from myapp.base_model import BaseModel, ActiveManager

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = ActiveManager() 
    all_objects = models.Manager()  

    def __str__(self):
        return self.name
