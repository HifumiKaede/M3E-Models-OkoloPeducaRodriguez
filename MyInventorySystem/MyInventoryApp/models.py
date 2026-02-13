from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def GetName(self):
        return self.name

    def __str__(self):
        f'Supplier: {self.name}, City: {self.city}, Country: {self.country}, Created At: {self.created_at}'
        