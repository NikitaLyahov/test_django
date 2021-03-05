from typing import Any

from django.views.generic.base import TemplateView

from orders.models import Orders


class TestPageView(TemplateView):
    template_name = 'test_view.html'

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        orders = Orders.objects.optimize()
        context['orders'] = orders
        context['query'] = orders.query
        return context
