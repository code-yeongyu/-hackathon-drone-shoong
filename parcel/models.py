from django.db import models


class Parcel(models.Model):
    PRODUCT_KIND_CHOICES = (('C', '의류'), ('D', '서신/서류'), ('E', '가전제품류'),
                            ('F', '과일류'), ('G', '곡물류'), ('M', '한약류'),
                            ('F', '식품류'), ('B', '잡화/서적류'), ('E', '기타'))
    # product info

    product_kind = models.CharField(choices=PRODUCT_KIND_CHOICES,
                                    null=False,
                                    blank=False,
                                    default='E',
                                    max_length=1)
    product_name = models.CharField(max_length=30, default='', null=False)
    product_price = models.IntegerField(null=False, default=0, blank=False)
    # sender
    sender_model = models.ForeignKey(
        'auth.user',
        related_name='parcel_user',
        on_delete=models.CASCADE,
        null=True,
    )
    sender_name = models.CharField(max_length=10, null=False, blank=False)
    sender_phone = models.CharField(max_length=12, null=False, blank=False)
    sender_phone_reservation = models.CharField(max_length=12,
                                                null=False,
                                                blank=False)
    sender_address = models.TextField(null=False, blank=False)
    requesting_text = models.TextField(null=True, blank=True)
    
    # recipient
    recipient_name = models.CharField(max_length=10, null=False, blank=False)
    recipient_phone = models.CharField(max_length=12, null=False, blank=False)
    recipient_address = models.TextField(null=False, blank=False)
    # etc
    created_at = models.DateTimeField(auto_now_add=True)
    #tracking_id = models.CharField(max_length=10, null=False, blank=False)
    #password = models.CharField(null=False, max_length=6)
    is_advance = models.BooleanField(default=False)
    # delivering status
    is_delivering = models.BooleanField(default=False)
    current_lat = models.FloatField(null=True, blank=True)
    current_long = models.FloatField(null=True, blank=True)