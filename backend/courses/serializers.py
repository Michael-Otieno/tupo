from .models import Course,User
from rest_framework import serializers





class UserSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields = ['id','first_name','last_name','id_number','phone_number','email','password','password2']

    extra_kwargs = {
      'password':{'write_only':True}
    }
  
  def validate(self, attrs):
    password = attrs.get('password')
    password2=attrs.pop('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email','password']
    


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = '__all__'