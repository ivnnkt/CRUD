from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CompanyViewSet, NewsViewSet, ProfileViewSet


router = SimpleRouter()

router.register(r'company', CompanyViewSet)
router.register(r'news', NewsViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]