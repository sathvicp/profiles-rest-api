from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({
            'message': 'HELLO',
            'an_apiview': an_apiview,
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                "message": message,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method: 'PUT'"}, status=status.HTTP_202_ACCEPTED)
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method: 'PATCH"}, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method: 'DELETE'"}, status=status.HTTP_202_ACCEPTED)
