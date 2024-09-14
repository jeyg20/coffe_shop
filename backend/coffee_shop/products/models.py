from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=100, verbose_name="name")
    description = models.TextField(max_length=300, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    available = models.BooleanField(default=True, verbose_name="available")
    creation_date_time = models.DateTimeField(
        auto_now_add=True, verbose_name="creation_date_time"
    )
    photo = models.ImageField(
        upload_to="images/products", null=True, blank=True, verbose_name="photo"
    )

    def __str__(self) -> str:
        return self.name
