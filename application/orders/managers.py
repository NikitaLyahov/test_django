from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import (
    Manager,
    Case,
    When,
    Func,
    Value,
    JSONField,
    QuerySet,
)


class OrdersManager(Manager):
    def optimize(self) -> QuerySet:
        queryset = super().get_queryset()
        return queryset.filter(
            status__paid=True,
            customer__emails__isnull=False
        ).values(
            'number',
            'status__paid',
            'customer__first_name',
            'customer__last_name',
            'customer__emails__address'
        ).annotate(
            products=ArrayAgg(Case(
                When(items__product__isnull=False, then=Func(
                    Value('product_name'), 'items__product__name',
                    Value('price'), 'items__product__price',
                    function='jsonb_build_object'
                )),
                default=Func(
                    Value('product_name'), 'items__non_customer_product__name',
                    Value('price'), 'items__non_customer_product__price',
                    function='jsonb_build_object'
                ),
                output_field=JSONField()
            ))
        )
