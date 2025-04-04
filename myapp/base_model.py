from django.db import models
from django.utils.timezone import now

class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(deleted_at=now(), is_deleted=True)

    def restore(self):
        return self.update(deleted_at=None, is_deleted=False)

class ActiveManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model).filter(is_deleted=False)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = ActiveManager()        # só ativos
    all_objects = models.Manager()   # acesso a todos

    class Meta:
        abstract = True

    def delete(self): 
        self.is_deleted = True
        self.deleted_at = now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.is_deleted = False
        self.save()
