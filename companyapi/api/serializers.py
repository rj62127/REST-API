from rest_framework import serializers
from api.models import Company,Employee

# Create Serializer here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    Company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"
        

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"