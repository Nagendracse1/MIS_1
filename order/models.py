from django.db import models


class OrderPoAndPurchaser(models.Model):

    po_no = models.CharField(max_length=255)
    Purchaser = models.CharField(max_length=130)
    po_date = models.CharField(max_length=255, null=True)


    class Meta:
        db_table = 'poAndPurchaser'
        verbose_name_plural='OrderPoAndPurchasers'

    def __str__(self):
        return self.po_no

    def get_authors(self):
        return (self.OrderDetails.all())


class OrderDetails(models.Model):

    OrderPoAndPurchaser = models.ForeignKey(
        OrderPoAndPurchaser,
        related_name='OrderDetails', on_delete=models.SET_NULL,
        null=True)

    po_date = models.CharField(max_length=255, null=True,blank=True)
    items = models.CharField(max_length=100,null=True)
    items_types = models.CharField(max_length=100,null=True)
    quality = models.CharField(max_length=100,null=True)
    qty = models.CharField(max_length=100,null=True)
    unit = models.CharField(max_length=100,null=True)
    rate_per_unit = models.CharField(max_length=100,null=True)
    value = models.CharField(max_length=100,null=True)
    dispatcher = models.CharField(max_length=100,null=True)

    dispatch_qty = models.CharField(max_length=100, blank=True, default='')
    dispatch_date = models.CharField(max_length=100, blank=True, default='')
    total_supplied_qty = models.CharField(max_length=100, blank=True, default='')
    balance_qty = models.CharField(max_length=100, blank=True, default='')




    class Meta:
        db_table = 'details'
        verbose_name_plural='OrderDetails'

    def __str__(self):
        return self.items



