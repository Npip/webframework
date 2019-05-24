from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def collec(request):
	if request.is_ajax():
		data=request.POST.get('data')
		with open('log.txt','r+') as file:
			file.write(str(data)+',')
			all = file.read()
			file.close()
			list =split(all.strip(','),',')
			return HttpResponse(json.dumps(list),content_type ='application/json')

def answer(request):
	if request.method =="POST":
		 data =request.POST.get()
		 with open('ceshi',"w")as f:
		 	f.write(data)
		 	f.close()
		 	return "hi"