from django.db import models
# Create your models here.

class Record(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50 , unique=True , default="")
    email = models.EmailField(max_length=50, unique=True , default="")
    notes = models.CharField(max_length=500, default="")

    def __str__(self):
        return (f"{self.first_name}")