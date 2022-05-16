from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or password is None:
        return Response({
            'Message': 'Login get data through form-data contentType'
        }, status=status.HTTP_204_NO_CONTENT)
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({
            'Message': 'User does not exist'
        }, status=status.HTTP_204_NO_CONTENT)

    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return Response({
            'Message': 'Your password or username are incorrect'
        }, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'token': token.key,
    }, status=status.HTTP_200_OK)
