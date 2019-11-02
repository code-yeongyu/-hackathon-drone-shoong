from rest_framework import serializers
from parcel.models import Parcel


class ParcelSerializerForUser(serializers.ModelSerializer):
    PRODUCT_KIND_CHOICES = (('C', '의류'), ('D', '서신/서류'), ('E', '가전제품류'),
                            ('F', '과일류'), ('G', '곡물류'), ('M', '한약류'),
                            ('F', '식품류'), ('B', '잡화/서적류'), ('E', '기타'))
    is_advance = serializers.BooleanField(default=False)
    product_kind = serializers.ChoiceField(required=True,
                                           choices=PRODUCT_KIND_CHOICES)
    product_name = serializers.CharField(required=True, max_length=30)
    product_price = serializers.IntegerField(required=True)

    is_delivering = serializers.ReadOnlyField()
    current_lat = serializers.ReadOnlyField()
    current_long = serializers.ReadOnlyField()

    class Meta:
        model = Parcel
        fields = ('id', 'product_kind', 'product_name', 'product_name',
                  'product_price', 'sender_model', 'sender_name',
                  'sender_phone', 'sender_phone_reservation', 'sender_address',
                  'requesting_text', 'recipient_name', 'recipient_phone',
                  'recipient_address', 'is_advance', 'is_delivering',
                  'current_lat', 'current_long')