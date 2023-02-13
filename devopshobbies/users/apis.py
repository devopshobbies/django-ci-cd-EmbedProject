from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from devopshobbies.users.models import BaseUser 

from drf_spectacular.utils import extend_schema


class RegisterApi(APIView):


    class InputRegisterSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(max_length=255)
        confirm_password = serializers.CharField(max_length=255)

    class OutPutRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaseUser 
            fields = ("email")

    @extend_schema(request=InputRegisterSerializer, responses=OutPutRegisterSerializer)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_user(
                    email=serializer.validated_data.get("email"),
                    password=serializer.validated_data.get("password"),
                    )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(self.OutPutRegisterSerializer(query, context={"request":request}).data)

