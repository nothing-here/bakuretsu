from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
           r'^home/$',
           views.smug_home,
           name='smug home'
       ),

    url(
           r'^browse/(?P<page_num>[0-9]+)/$',
           views.browse,
           name='browse'
       ),

    url(
           r'^images/(?P<image_id>[0-9]+)/$',
           views.disp_image,
           name='display image'
       ),

    url(
           r'^search/$',
           views.search,
           name='search'
       ),

    url(
           r'upload/$',
           views.upload,
           name='upload'
       ),

    url(
           r'^test/$',
           views.test,
           name='test'
       ),
]
