from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, UserSerializer

#ENDPOINT: Create an user
@api_view(['POST'])
def registerUser(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'User registered succesfully'}, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#ENDPOINT: Get all tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTasks(request):
    tasks = Task.objects.filter(user = request.user)
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

#ENDPOINT: Create a task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#ENDPOINT: Update an existing task
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTask(request, pk):
    try:
        task = Task.objects.get(pk = pk, user=request.user)
    except:
        return Response({'error': 'Task not found'}, status= status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(instance = task, data = request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_200_OK)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#ENDPOINT: Delete an existing task
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    try:
        task = Task.objects.get(pk = pk, user=request.user)
    except:
        return Response({'error': 'Task not found'}, status= status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response({'message': 'Task deleted succesfully'}, status=status.HTTP_200_OK)


    