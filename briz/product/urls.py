from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    # /index
    url(r'^$', views.index, name='index'),

    # /omoss
    url(r'^omoss/$', views.contact, name='contact'),

    # /product_type/product_id, /dress/1
    url(r'^(?P<product_type>[a-zA_Z]+)/(?P<product_id>[0-9]+)/$', views.detail, name='detail'),

    # /product_type, /dress
    url(r'^(?P<product_type>[a-zA_Z]+)/$', views.collection, name='collection'),

    # /10-tips-til-bryllupet
    url(r'^10-tips-til-bryllupet/$', views.tips, name='tips'),

    # /slik-skal-dressen-sitte
    url(r'^slik-skal-dressen-sitte/$', views.dressen_sitte, name='dressen_sitte'),

    # /dress-guide-for-menn
    url(r'^dress-guide-for-menn/$', views.dress_guide, name='dress_guide'),
]

