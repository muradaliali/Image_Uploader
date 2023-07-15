from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    Img = Image.objects.all()
    return render(request,'myapp/index.html',{"img":Img,'form':form})

# Create your views here.
