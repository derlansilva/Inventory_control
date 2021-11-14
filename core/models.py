from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'created at ...',
        auto_now_add= True,
        auto_now= False
    )

    modified = models.DateTimeField(
        'modified at' ,
        auto_now_add=  False,
        auto_now=True
    )

class Meta:
    abstract = True