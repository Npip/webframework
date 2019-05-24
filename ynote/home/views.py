from django.shortcuts import render

# Create your views here.
def proc(request):
    return render(request, 'index.html')
