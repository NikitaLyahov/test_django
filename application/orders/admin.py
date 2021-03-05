from django.contrib import admin

from orders.models import (
    Orders,
    Status,
    Items,
)


admin.site.register(Orders)
admin.site.register(Status)
admin.site.register(Items)
