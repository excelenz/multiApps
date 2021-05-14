from django.contrib import admin
from .models import Customer
from django.contrib import admin


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ("name", "id_customer","created_on")

    class Meta:
        ordering = ("created_on", "name")

    def show_unchangable_data_from_biostar2(self, obj):
        result = Customer.objects.filter(id_customer=obj)
        return "ddd"

#admin.site.register(Customer)
