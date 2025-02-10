from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import ComanySerializers,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

# Create your company views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class= ComanySerializers

#   companies/{companyId}/employee
    @action(detail=True, methods = ["get"])
    def employee (self, request,pk= None ):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emp_serialozer = EmployeeSerializer(emps,many = True, context={'request':request})
            return Response(emp_serialozer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exist'
            })



# Create your company views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer