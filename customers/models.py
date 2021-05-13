from django.db import models

class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
