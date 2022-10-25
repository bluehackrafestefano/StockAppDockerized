from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Stock, Product

@receiver(pre_save, sender=Stock)
def pre_save_create_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        instance.price_total = instance.quantitiy * instance.price


@receiver(post_save, sender=Stock)
def pre_save_update_stock(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product_id)
    if instance.transaction == 'I':
        if not product.stock:
            product.stock = instance.quantitiy
        else:
            product.stock += instance.quantitiy
    else:
        product.stock -= instance.quantitiy
    product.save()
