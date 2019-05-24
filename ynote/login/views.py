"""
encoding =utf-8
"""
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import render
# Create your views here.
def proc(request):
	request.encoding= 'utf-8'
	if request.method == "POST":
		username =request.POST["username"]
		password =request.POST["password"]
		data={
			"username":username,
			"password":password
		}
		return JsonResponse(data)
	elif request.method == "GET":
		return render(request, 'login.html')
	else:
		return HttpResponse("sorry error method")