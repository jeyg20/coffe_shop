from django.urls import path

from .views import CreateORderProtductView, MyOrderView

urlpatterns = [
    path("my-order", MyOrderView.as_view(), name="my_order"),
    path("add-product", CreateORderProtductView.as_view(), name="add_product"),
]
