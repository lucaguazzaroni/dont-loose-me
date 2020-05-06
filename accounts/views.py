import json 

from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login

from rest_framework import status


def account_login(request):
	if request.method == 'POST':
		post_data = json.loads( request.body.decode("UTF-8") )
		
		user = authenticate(
			request,
			username = post_data.get('username'), 
			password = post_data.get('password')
		)
		
		if user is not None:
			if user.is_active:
				login(request, user)
				return JsonResponse({"msg":"login success"}, safe=False, status=status.HTTP_200_OK)
		else:
			return JsonResponse({"msg":"login fail"}, safe=False, status=status.HTTP_401_UNAUTHORIZED)


def account_logout(request):
	logout(request)
	return JsonResponse({"msg":"logout success"}, safe=False, status=status.HTTP_200_OK)




