from rest_framework import serializers

from api.models import DataPoint


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = '__all__'
