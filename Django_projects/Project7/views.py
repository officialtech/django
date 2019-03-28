from django.shortcuts import render

# Create your views here.

def indexPage(r):
    return render(r, 'index.html')




def details(request):
    name = request.POST.get("name1")
    age = request.POST.get("age1")
    contact = request.POST.get("c1")
    gender = request.POST.get("rd")
    subject = request.POST.getlist("s1")

    if len(subject) == 1 and subject[0] == 'Core Python':
        subject = "Core Python is free, So select atleast one Other subject"
    else:
        if subject == []:
            subject = "Subject shouldn't empty"

    faculty = request.POST.get("teachers")
    name1 = request.POST.get("nam")
    password = request.POST.get("pas")

    d ={
        "n": name, "a": age, "c": contact, "g": gender, "s": subject, "fac": faculty, "name": name1, "passw": password
    }

    return render(request, 'newOne.html', {"key1": d})