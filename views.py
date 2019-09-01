from django.shortcuts import render

def showIndex(req):
    return render(req,"index.html")


def showData(request):
    item = request.POST.get("rb")
    return render(request,"index.html",{"message":item})