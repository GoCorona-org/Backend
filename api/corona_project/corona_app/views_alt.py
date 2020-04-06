from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from corona_app.models import CoronaApp
from corona_app.serializers import CoronaAppSerializer


@api_view(['GET', 'POST'])
def CoronaApp_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        covids = CoronaApp.objects.all()
        serializer = CoronaAppSerializer(covids, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoronaAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def CoronaApp_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        covid = CoronaApp.objects.get(pk=pk)
    except CoronaApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoronaAppSerializer(covid)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoronaAppSerializer(covid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        covid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)