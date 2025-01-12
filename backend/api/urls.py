from django.urls import path, include
from .views import UserViewSet, BotUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'botusers', BotUserViewSet, basename='botuser')


urlpatterns = [
    path('', include(router.urls)),
    
]