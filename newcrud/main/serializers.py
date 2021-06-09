from rest_framework import serializers
from .models import Company, Profile, News


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    company_name = serializers.SlugRelatedField(slug_field="name", read_only=True)
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.SlugRelatedField(slug_field="username", read_only=True)
    company = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
