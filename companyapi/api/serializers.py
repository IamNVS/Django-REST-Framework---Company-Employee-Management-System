from rest_framework import serializers
from api.models import Company,Employee
# Crete serializers 


# Crete Company serializers 

class ComanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

# Crete Employee serializers 

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"