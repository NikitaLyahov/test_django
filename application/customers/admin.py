from django.contrib import admin

from customers.models import (
    Customers,
    Emails,
)


admin.site.register(Customers)
admin.site.register(Emails)
