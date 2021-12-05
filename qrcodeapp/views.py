from django.shortcuts import render,redirect
import qrcode
from resizeimage import resizeimage


def home(request):
    if request.method=="POST":
        id=request.POST.get("sid")
        name=request.POST.get("sname")
        email=request.POST.get("email")
        course=request.POST.get("course")
        img=qrcode.make(f"Student Id:{id}\nStudent Name:{name}\nStudent Email:{email}\nCourse:{course}")
        img=resizeimage.resize_cover(img,[300,300])
        img.save('static/some_file.png')
    else:
        img = qrcode.make("No data is there")
        img = resizeimage.resize_cover(img, [300, 300])
        img.save('static/some_file.png')

    return render(request,'home.html')
def clear(request):
    img=qrcode.make("No data is there")
    img=resizeimage.resize_cover(img,[300,300])
    img.save('static/some_file.png')
    return redirect('home')

# Create your views here.
