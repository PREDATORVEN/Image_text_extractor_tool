from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.http import JsonResponse
from PIL import Image
from pytesseract import pytesseract
import os
from django.conf import settings

# Define path to Tesseract executable
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def home_page(request):
    return render(request,'upload.html')

def image_upload(request):
    if request.method=='POST'and request.FILES['image']:
        image=request.FILES['image']
        fs=FileSystemStorage()
        file_name=fs.save(image.name,image)
        image_url=fs.url(file_name)
        full_path=os.path.join(settings.MEDIA_ROOT,file_name)
        img_path=Image.open(full_path)
        pytesseract.tesseract_cmd=path_to_tesseract
        image_text=pytesseract.image_to_string(img_path)
    
        return render(request,'preview.html',{'image_url':image_url,'image_text':image_text})
    