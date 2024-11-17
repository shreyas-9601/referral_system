from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'mobile_number', 'city', 'referral_code', 'password']

    def validate(self, data):
        if not data.get('email') or not data.get('name') or not data.get('mobile_number') or not data.get('city') or not data.get('password'):
            raise serializers.ValidationError("All fields are mandatory.")
        
        if data.get('referral_code'):
            try:
                referrer = User.objects.get(referral_code=data['referral_code'])
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid referral code.")
            data['referrer'] = referrer
        return data

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'date_joined']