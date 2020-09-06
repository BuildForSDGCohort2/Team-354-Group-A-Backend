from rest_framework import serializers
from .models import useraccount


class userSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = useraccount
        fields = ["email", "first_name", "last_name",
                  "phone_number", "password", "password2"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = useraccount(
            email=self.validated_data['email'],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            phone_number=self.validated_data["phone_number"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"password": "passwords should match"})
        user.set_password(password)
        user.save()
        return user


class userpropertiesserializer(serializers.ModelSerializer):
    class Meta:
        model = useraccount
        fields = fields = ["pk", "email",
                           "first_name", "last_name", "phone_number"]
