from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<id>[0-9]+)/$',views.detail, name='detail'),
    #url(r'^', views.index, name='index'),
    url(r'^goodslist/(?P<typeId>[0-9]+)_(?P<pIndex>[0-9]+)/$',views.goodslist,name='goodslist'),
]
