from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=['Male', 'Female', 'Other'])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age', 'gender')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive number.")
        return value

    def validate_gender(self, value):
        if value not in ['Male', 'Female', 'Other']:
            raise serializers.ValidationError("Gender must be one of the following: Male, Female, Other.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # Custom fields like age and gender can be stored in a UserProfile model if necessary
        # user.profile.age = validated_data['age']
        # user.profile.gender = validated_data['gender']
        # user.profile.save()
        return user
