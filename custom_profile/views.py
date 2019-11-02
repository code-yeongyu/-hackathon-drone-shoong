from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, mixins

from custom_profile.forms import SignUpForm
from custom_profile.models import Profile
from custom_profile.serializers import ProfileSerializer
from dicon import settings


class ProfileAPIView(APIView):
    """
        프로필 조회
        ---
        # 내용
            - name: string: 이름
            - address: string: 주소
            - phone : digit, max_length=12: 전화번호
    """
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):  # 프로필 조회
        profile = Profile.objects.get(user=request.user)

        return Response(ProfileSerializer(profile).data,
                        status=status.HTTP_200_OK)
    
    def patch(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_406_NOT_ACCEPTABLE)


def sign_up(request):  # 회원가입
    form = SignUpForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
