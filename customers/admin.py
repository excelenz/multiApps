from django.contrib import admin
from .models import Customer
import random


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "id_customer","created_on","show_biostar2")

    class Meta:
        ordering = ("created_on", "name")

    def show_biostar2(self, obj): #show_unchangable_data_from_biostar2
        print(obj)
        result = Customer.objects.get(name=obj)
        return str(random.randrange(100000, 1000000)) + "user_id" + result.id_customer
    show_biostar2.short_description = "Unchangeable data"

#admin.site.register(Customer)
