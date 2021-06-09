from rest_framework.permissions import IsAdminUser
from .models import Company, Profile, News
from .permissions import IsStaffOrReadOnly, IsOwnerOrStaffOrReadOnly
from .serializers import CompanySerializer, NewsSerializer, ProfileSerializer
from rest_framework.viewsets import ModelViewSet


class CompanyViewSet(ModelViewSet):

    queryset = Company.objects.all()
    permission_classes = [IsStaffOrReadOnly]
    serializer_class = CompanySerializer


class NewsViewSet(ModelViewSet):

    queryset = News.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class ProfileViewSet(ModelViewSet):

    queryset = Profile.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ProfileSerializer
