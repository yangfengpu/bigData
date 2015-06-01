from django.conf.urls import url

from . import views
urlpatterns = [
    # ex: /cococloud/
    url(r'^$', views.index, name='index'),
    # ex: /cococloud/alf/
    url(r'^alf/$', views.alf, name='alf'),
    # ex: /cococloud/alf/5/
    url(r'^alf/(?P<yv_id>[0-9]+)/$', views.detail, name='detail'),

    ]