# topsites/serializers.py

from rest_framework import serializers
from .models import TopSite

class TopSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopSite
        fields = '__all__'
