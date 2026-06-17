from django.db import models
from accounts.models import StoreUsers


class StoreCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StoreProduct(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, db_index=True)
    sku = models.CharField(max_length=50, unique=True)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(
        StoreCategory,
        on_delete=models.CASCADE,
        related_name="products"
    )

    created_by = models.ForeignKey(
        StoreUsers,
        on_delete=models.CASCADE,
        related_name="products"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StoreComment(models.Model):

    class Rating(models.IntegerChoices):
        ONE = 1, "1 Star"
        TWO = 2, "2 Stars"
        THREE = 3, "3 Stars"
        FOUR = 4, "4 Stars"
        FIVE = 5, "5 Stars"

    product = models.ForeignKey(
        StoreProduct,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
        StoreUsers,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    comment = models.TextField()

    rating = models.IntegerField(
        choices=Rating.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class StoreProductImage(models.Model):
    product = models.ForeignKey(
        StoreProduct,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="products/"
    )

    is_primary = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)