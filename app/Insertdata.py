from app.models import student


from django.shortcuts import render


def Insertdata(request):
    if request.method=="POST":
        name=request.post.get('name')
        email=request.post.get('email')
        age=request.post.get('age')
        gender=request.post.get('gender')
        query=student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render(request,"index.html")