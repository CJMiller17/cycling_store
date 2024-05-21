from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.db import transaction
from .models import *
from .serializers import *

class InventoryViewSet(viewsets.ModelViewSet): #This is the end point
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class CustomerViewSet(viewsets.ModelViewSet): #This is the end point
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# def get_letter_grade(obj):
#         if (obj.score >= 90):
#             return 'A'
#         elif (obj.score >= 80):
#             return 'B'
#         elif (obj.score >= 70):
#             return 'C'
#         elif (obj.score >= 60):
#             return 'D'
#         else:
#             return 'F'

class OrderViewSet(viewsets.ModelViewSet): #This is the end point
    queryset = Order.objects.all() # Used to retrieve data from the database
    serializer_class = OrderSerializer 

    def create(self, request):
        mutable_data_copy = request.data.copy()
        item_id = mutable_data_copy.get('item')
        item = Inventory.objects.get(pk=item_id) # The two tables talk to each other now
        qty_ordered = int(mutable_data_copy.get('qty'))

        serializer = self.get_serializer(data=mutable_data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        item.in_stock -= qty_ordered
        item.save()
        
        return Response(serializer.data)
        
    
    
 # def destroy(self, request, pk=None):
    #     course = self.get_object()
    #     if Grade.objects.filter(course=course).exists():
    #         raise ValidationError({'detail': 'Cannot Delete Course because it has associated grades'})
        
    #     self.perform_destroy(course)
    #     return Response()

# class GradeViewSet(viewsets.ModelViewSet): #This is the end point
#     queryset = Grade.objects.all()
#     serializer_class = GradeSerializer

#     def retrieve(self, request, pk = None):
#         grade = Grade.objects.get(pk=pk)
#         grade_serializer = GradeSerializer(grade)
#         data = grade_serializer.data
#         data['letter_grade'] = get_letter_grade(grade)
#         print('HERE: ', data)
#         return Response(data)
    
#     def update(self, request, pk= None):
#         grade = Grade.objects.get(pk=pk)
#         grade_serializer = GradeSerializer(data = request.data)
#         grade_serializer.is_valid(raise_exception=True)
#         grade_serializer.save()

#         student = Student.objects.get(id= grade.student.id)
#         if (int(request.data['score']) > 90):
#             if not student.name.startswith('Brilliant'):
#                 student.name = f'Brilliant {student.name}'
#                 student.save()
#             else:
#                 if student.name.startswith('Brilliant'):
#                     student.name = student.name.replace('Brilliant ', '')
#                     student.save()
                
#         return Response(grade_serializer.data)