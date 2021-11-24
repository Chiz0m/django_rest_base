# import receipt
# from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response, responses
# from .serializers import NewUserSerializer, UpdateBizSerializer
# from .models import NewUser

# # Create your views here.
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def updateBusinessName(request,pk):
#     business = NewUser.objects.get(id=pk)
#     serializer = UpdateBizSerializer(business, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.error_messages)