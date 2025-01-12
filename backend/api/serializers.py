from users.models import User, Profile, OneTimeCode
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']

    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'username', 'bio', 'image', 'created_at', 'updated_at']


class OneTimeCodeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = OneTimeCode
        fields = ['id', 'user', 'code', 'created_at', 'updated_at', 'is_used']


class OneTimeCodeLoginSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    
    def validate(self, data):
        code = data.get('code')

        if not code:
            raise serializers.ValidationError({'code': 'This field is required.'})

        one_time_code = OneTimeCode.objects.filter(code=code, is_used=False).first()
        if not one_time_code:
            raise serializers.ValidationError({'code': 'Invalid code.'})
        
        return data
    
    def create(self, validated_data):
        code = validated_data.get('code')
        
        one_time_code = OneTimeCode.objects.filter(code=code, is_used=False).first()
        one_time_code.is_used = True
        one_time_code.save()
        
        user = one_time_code.user
        return user