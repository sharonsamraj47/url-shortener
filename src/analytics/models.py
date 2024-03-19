from django.db import models

# Create your models here.

from shortener.models import KirrUrl

class ClickEventManager(models.Manager):
    def create_event(self, Kirrinstance):
        if isinstance(Kirrinstance, KirrUrl):
            obj, created = self.get_or_create(Kirr_url=Kirrinstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    Kirr_url = models.OneToOneField(KirrUrl,on_delete=models.CASCADE)
    count    = models.IntegerField(default=0)
    updated  = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
        
