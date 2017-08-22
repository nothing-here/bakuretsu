from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ImageDetails, ImageTag
# Create your views here.

def smug_home(request):
    newest_imgs_r1 = ImageDetails.objects.all()[:4]
    newest_imgs_r2 = ImageDetails.objects.all()[4:8]
    template = loader.get_template('l/main.html')
    context = {
       'newest_imgs_r1': newest_imgs_r1,
       'newest_imgs_r2': newest_imgs_r2,
    } 
    return HttpResponse(template.render(context, request))

def browse(request, page_num):
    try:
        page_num = int(page_num)*2
    except:
        return HttpResponse('ERROR: Non-numeric string after /browse')
    newest_imgs_r1 = ImageDetails.objects.all()[page_num*4:(page_num+1)*4]
    newest_imgs_r2 = ImageDetails.objects.all()[(page_num+1)*4:(page_num+2)*4]
    template = loader.get_template('l/main.html')
    context = {
       'newest_imgs_r1': newest_imgs_r1,
       'newest_imgs_r2': newest_imgs_r2,
    } 
    return HttpResponse(template.render(context, request))

def disp_image(request, image_id):
    img = ImageDetails.objects.get(pk=image_id)
    tags = ImageTag.objects.filter(image_id=img)
    template = loader.get_template('l/disp_image.html')
    context = {
        'img': img,
        'tags': tags,
    }
    return HttpResponse(template.render(context, request))

def test(request):
    template = loader.render_to_string('l/test.html')
    return HttpResponse(template)
