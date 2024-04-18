from django.shortcuts import render
from mysite.models import Person 
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def mydata(request):
    if request.method == 'GET':
        Persons = Person.objects.all()  
        serializer = PersonSerializer(Persons, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def sentdata(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
     
        if serializer.is_valid():
            serializer.save()  # Save the validated data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def removedata(request):
    if request.method == 'DELETE':
        person_id = request.query_params.get('id')
        try:
            person = Person.objects.get(id=person_id)  # Rename the variable to avoid naming conflict
            person.delete()
            return Response({"success": "Person deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
