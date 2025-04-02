from django.db import models
from django.utils.timezone import now

class BaseModel(models.Model):
    
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True  

    def delete(self, *args, **kwargs): 
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
