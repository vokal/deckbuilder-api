from rest_framework import generics, status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from user.serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):

    serializer_class = UserCreateSerializer
    queryset = get_user_model()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
