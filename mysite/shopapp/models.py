from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def product_preview_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Product(models.Model):
    """
    Модель Product представляет товар,
    который можно продавать в интернет-магазине.

    Заказы тут: :model:`shopapp.Order`
    """
    objects = None
    orders = None

    class Meta:
        ordering = ["name", "price"]
        verbose_name = "product"
        verbose_name_plural = "products"

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True, db_index=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    discount = models.SmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path)

    def get_absolute_url(self):
        return reverse("shoppapp:product_details", kwargs={"pk": self.pk})

    @property
    def description_short(self) -> str:
        if len(self.description) < 48:
            return self.description
        return self.description[:48] + "..."

    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=product_images_directory_path)
    description = models.CharField(max_length=200, null=False, blank=True)


class Order(models.Model):

    objects = None

    class Meta:
        ordering = ["user"]
        verbose_name = "order"
        verbose_name_plural = "orders"

    delivery_adress = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
    archive = models.BooleanField(default=False)
    receipt = models.FileField(null=True, upload_to='orders/receipts/')
