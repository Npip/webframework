from django.shortcuts import render

# Create your views here.
def proc(request):
    #为新访客添加数据
    if request.method=="GET":
        return render(request,'qd.html')
    elif request.method=="POST":
        imei=request.POST.get("imei")
        position=request.POST.get("position")

