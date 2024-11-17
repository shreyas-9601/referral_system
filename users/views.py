from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserRegistrationSerializer
from .serializers import ReferralSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'id': user.id, 'referral_code': user.referral_code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return Response({'id': user.id, 'email': user.email}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def get_referral_users(request, referral_code):
    if request.method == 'GET':
        users = User.objects.filter(referrer__referral_code=referral_code)
        serializer = ReferralSerializer(users, many=True)
        return Response(serializer.data)

