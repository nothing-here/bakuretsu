from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods, require_safe

from .models import ImageDetails, ImageTag

# Create your views here.

@require_http_methods(['GET','HEAD'])
def smug_home(request):
    newest_imgs = ImageDetails.objects.all()[:8]
    template = loader.get_template('l/main_page.html')
    context = {
       'imgs': newest_imgs,
    } 
    return HttpResponse(template.render(context, request))

@require_http_methods(['GET','HEAD'])
def browse(request, page_num):
    try:
        page_num = int(page_num)
    except:
        return HttpResponse('ERROR: Non-numeric string after /browse')
    newest_imgs = ImageDetails.objects.all()[8+page_num*16:8+page_num+1*16]
    template = loader.get_template('l/gallery.html')
    context = {
       'imgs': newest_imgs,
    } 
    return HttpResponse(template.render(context, request))

@require_http_methods(['GET','HEAD'])
def disp_image(request, image_id):
    img = ImageDetails.objects.get(pk=image_id)
    tags = ImageTag.objects.filter(image_id=img)
    template = loader.get_template('l/disp_image.html')
    context = {
        'img': img,
        'tags': tags,
    }
    return HttpResponse(template.render(context, request))

@require_http_methods(['GET','HEAD'])
def search(request):
    search_str = ""
    try:
       search_str = request.GET.__getitem__('search_term')
    except Exception as e:
        return HttpResponse('ERROR ' + str(e))
    imgs = find_imgs_from_str(search_str)
    tags_list = []
    try:
        for img in imgs:
            tags_list.append(ImageTag.objects.filter(image_id=img))
    except Exception as e:
        return HttpResponse('ERROR'+str(e))
    template = loader.get_template('l/gallery.html')
    context = {
        'imgs': imgs,
        'tags_list': tags_list,
    }
    return HttpResponse(template.render(context, request))

@require_http_methods(['GET','POST'])
def upload(request):
    if(request.method == 'GET'):
        return HttpResponse(render(request,'l/test.html'))
    elif(request.method == 'POST'):
        string = ""
        for entry in request.POST:
            string += str(entry)+ '\n'
        if(request.FILES != None):
            string += 'File is attached\n'
        return HttpResponse(string)

def test(request):
    template = loader.render_to_string('l/test.html')
    return HttpResponse(template)

#---------------------------
# Helpers
#---------------------------
def tokenize_str(search_string):
    """
    Quick processing for tokenizing
    All it does is split at whitespace
    Arguments:
        search_string - string to tokenize
    Returns:
        list of tokenized strings
    """

    tokens = search_string.split()
    for i in range(0,len(tokens)):
        tokens[i] = tokens[i].strip()

    return tokens

def keyword_to_img(keyword):
    """
    THIS A HACK V1
    --------------
    returns all pictures that have tags that matches works in a search string
    Arguments:
        tag - tokenized keyword
    Returns:
        list of ImageDetails objects
    """

    imgs = []

    #TODO: change matching algorithm once more sophisticated
    #NOTE: cannot take out all database entries and then fuzzy match, find workaround
    tags = ImageTag.objects.filter(tag=keyword.lower())

    for tag in tags:
        imgs.append(tag.image_id)

    return imgs

def find_imgs_from_str(search_string):
    """
    Tokenizes search string and matches image objects
    Arguments:
        search_string - string to search
    Returns:
        list of ImageDetails objects
    """

    imgs = []

    tokens = tokenize_str(search_string)

    for keyword in tokens:
        keyword_matchs = keyword_to_img(keyword)
        for match in keyword_matchs:
            imgs.append(match)

    return imgs
