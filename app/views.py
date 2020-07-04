from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerailizer


# Create your views here.
class UserView(APIView):

    def get(self, request):

        users = User.objects.prefetch_related('activity_periods').all()
        context = UserSerailizer(users, many=True)

        return Response(context.data)
