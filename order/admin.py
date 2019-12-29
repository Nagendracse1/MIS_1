from django.contrib import admin
from .models import OrderPoAndPurchaser,OrderDetails
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(OrderDetails)

@admin.register(OrderPoAndPurchaser)
class OrderPoAndPurchaser(ImportExportModelAdmin):
    pass



