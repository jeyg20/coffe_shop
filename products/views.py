from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from products.forms import ProductForm
from products.models import Product
from products.serializers import ProductSerializer


class ProductFormView(FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"


class ProducListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
