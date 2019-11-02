from rest_framework import generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from parcel.models import Parcel
from parcel.serializers import ParcelSerializerForUser


class ParcelListCreateAPIView(APIView):
    """
        택배 생성 | 내가 신청한 택배 조회
        ---
        # 내용
            - product_kind: options, ('C', '의류'), ('D', '서신/서류'), ('E', '가전제품류'),
                            ('F', '과일류'), ('G', '곡물류'), ('M', '한약류'),
                            ('F', '식품류'), ('B', '잡화/서적류'), ('E', '기타'): 제품 종류
            - product_name: string, max_length=30: 제품 이름
            - product_price: integer: 만원 단위 가격
            - sender_name: string: 보낸이 이름
            - sender_phone: digit, max_length=12: 보낸이 전화번호
            - sender_phone_reservation: digit, max_length=12: tracking id받을 전화번호
            - sender_address: digit, max_length=12: 보낸이 주소
            - requesting_text: string: 배송 요청사항
            - recipient_name: string: 받는이 이름
            - recipient_phone: digit, max_length=12: 받는이 전화번호
            - recipient_address: digit, max_length=12: 받는이 주소
            - is_advance: boolean: 선불인지 여부
            - tracking_id: string: 트래킹 ID | 비활성화 됨
            - password: string: 조회시 필요한 비밀번호 | 비활성화 됨
            ## ReadOnly
            - is_delivering: boolean: 현재 배송중인지 여부
            - current_lat: float: 현재 택배 좌표 latitude
            - current_long: float: 현재 택배 좌표 longtitude
    """
    def get(self, request):
        if request.user.is_authenticated:
            parcel = Parcel.objects.filter(sender_model=request.user.id, )
            return Response(ParcelSerializerForUser(parcel, many=True).data,
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ParcelSerializerForUser(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(sender_model=request.user)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=HTTP_406_NOT_ACCEPTABLE)

class ParcelDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializerForUser

# tracking id and password authentication is required when making tracking algorithm is done