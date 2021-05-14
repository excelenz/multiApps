from django.contrib import admin
from .models import Customer
import random
from . face_data import integration


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "id_customer","created_on","show_biostar2")

    class Meta:
        ordering = ("created_on", "name")

    def show_biostar2(self, obj): #show_unchangable_data_from_biostar2
        face = integration()
        result = Customer.objects.get(name=obj)
        payload={'id_customer':result.id_customer,'customer_name':result.name,'method':'get'}
        data = face.call_to_biostar2(**payload)
        return str(random.randrange(100000, 1000000)) + " user_id " + str(result.id_customer)
    show_biostar2.short_description = "Unchangeable data // fingerprint_template_count"

#admin.site.register(Customer)
