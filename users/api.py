from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from twilio.rest import Client
import random
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_throttles(self):
        if self.action == "update":
            # aca vamos a decir que use el throttle_scope
            self.throttle_scope = "generate_code"
        return super().get_throttles()
            
    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        code = random.randint(1000, 9999)
        # si queremos aumentar datos al request primero debemos hacerlo mutable
        request.data._mutable = True
        request.data["code"] = code
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            # twilio credentials
            TWILIO_ACCOUNT_SID = "use_from_twilio"
            TWILIO_AUTH_TOKEN = "use_from_twilio"
            Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN).messages.create(
                messaging_service_sid='use_from_twilio', 
                body=f"Tu codigo es {code}",      
                to='+51967617166'
            )

            serializer.save()
            return Response({
                "ok": True,
                "message": "user updated"
            })


class UserViewGenericViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def retrieve(self, request, *args, **kwargs):
        print(request)
        return super().retrieve(request, *args, *kwargs)
