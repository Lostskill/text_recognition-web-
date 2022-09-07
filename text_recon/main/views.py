from django.shortcuts import render
from .forms import ImageForm
# Create your views here.
from PIL import Image
from pytesseract import pytesseract

def image_upload(request):
    context = dict()

    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['file_upload'])
            image_text = pytesseract.image_to_string(image,lang='rus')
            image_picture = handle_uploaded_file(request.FILES['file_upload'])

            
            context.update({'image_text':image_text,'image_pic':image_picture })
            
            form = ImageForm()    
    else:
    
        form = ImageForm()
    
    context.update({'form':form,})
    print(context)
    return render(request,'main/index.html',context)

def handle_uploaded_file(f):
    with open('main/static/main/images/need_pic.png', 'wb+') as destination:
        for chunk in f.chunks() :
            destination.write(chunk)
    


    