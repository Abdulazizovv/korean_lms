from .serializers import UserSerializer, OneTimeCodeLoginSerializer, BotUserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from users.models import User, OneTimeCode
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from botapp.models import BotUser



class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='login', url_name='login')
    def login(self, request):
        serializer = OneTimeCodeLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    @action(detail=False, methods=['post'], url_path='register', url_name='register')
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='refresh', url_name='refresh')
    def refresh(self, request):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'refresh': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh)
        except Exception as e:
            return Response({'refresh': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'access': str(refresh.access_token),
        })

    @action(detail=False, methods=['post'], url_path='logout', url_name='logout', permission_classes=[IsAuthenticated])
    def logout(self, request):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'refresh': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh)
        except Exception as e:
            return Response({'refresh': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
        refresh.blacklist()
        return Response({'message': 'Logout successful.'})
    

class BotUserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='exists', url_name='exists')
    def exists(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'user_id': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if BotUser.objects.filter(user_id=user_id).exists():
            return Response({'exists': True})
        return Response({'exists': False})


    @action(detail=False, methods=['post'], url_path='register', url_name='register')
    def register(self, request):
        serializer = BotUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bot_user = serializer.save()
        return Response({
            'id': bot_user.id,
            'user_id': bot_user.user_id,
            'first_name': bot_user.first_name,
            'last_name': bot_user.last_name,
            'username': bot_user.username,
            'language_code': bot_user.language_code,
            'is_active': bot_user.is_active,
            'created_at': bot_user.created_at,
            'updated_at': bot_user.updated_at,
        }, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='refresh', url_name='refresh')
    def refresh(self, request):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'refresh': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh)
        except Exception as e:
            return Response({'refresh': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'access': str(refresh.access_token),
        })

    @action(detail=False, methods=['post'], url_path='logout', url_name='logout', permission_classes=[IsAuthenticated])
    def logout(self, request):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'refresh': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh)
        except Exception as e:
            return Response({'refresh': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
        refresh.blacklist()
        return Response({'message': 'Logout successful.'})