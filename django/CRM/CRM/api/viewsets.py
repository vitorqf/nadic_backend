from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from CRM.api.serializers import UserSerializer


class UserViewSet(ViewSet):
    def get_permissions(self):
        if self.action == "create" or self.action == "login":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        token, _ = Token.objects.get_or_create(user=user)

        if user is None:
            return Response(
                {"error": "Invalid data"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"token": user.auth_token.key},
            status=status.HTTP_200_OK,
        )

    def logout(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        is_staff = self.request.data.get("is_staff", False)
        user = serializer.save(is_staff=is_staff)
        (user)
        user.is_staff = is_staff
        user.save()

    def set_staff(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if not request.user.is_superuser:
            return Response(
                {"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN
            )

        is_staff = request.data.get("is_staff", False)
        user.is_staff = is_staff
        user.save()

        return Response(
            {"detail": "User staff status updated successfully"},
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if not request.user.is_superuser:
            return Response(
                {"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN
            )
        serializer = UserSerializer(user)
        return Response(
            {"is_staff": user.is_staff, "user": serializer.data},
            status=status.HTTP_200_OK,
        )
