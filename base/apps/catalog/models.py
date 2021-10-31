from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name="Brand name")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    """
    A product should have basic info such as sku, name, price and brand
    """

    sku = models.CharField(
        max_length=200,
        verbose_name="Stock Keeping Unit",
        help_text="Stock Keeping Unit",
    )
    name = models.CharField(max_length=200, verbose_name="Product name")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.sku

    def __unicode__(self):
        return self.sku


class ProductCounter(models.Model):
    """
    Keep track of the number of times every single product is queried by an anonymous user, so we can build some reports in the future.
    """

    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    counter = models.IntegerField(verbose_name="Counter")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product counter"
        verbose_name_plural = "Product counters"


class ProductTracker(models.Model):
    """
    Keep track of the number of times every single product is queried by an anonymous user, so we can build some reports in the future.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    useragent = models.CharField(
        max_length=500, verbose_name="useragent", help_text="Trackinfor by User"
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product tracker"
        verbose_name_plural = "Product trackers"
