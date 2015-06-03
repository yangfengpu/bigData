from django.conf.urls import url, include


from . import views

urlpatterns = [

    
    # ex: /cococloud/
    url(r'^$', views.index, name='index'),

    #------ Activity (triple)--------------
    # ex: /cococloud/activities/
    url(r'^activities/$', views.activities, name='activities'),
    # ex: /cococloud/createActivities/
    url(r'^createActivities/$', views.createActivity, name='createActivities'),
    #ex: /cococloud/updateActivity/5/
    url(r'^updateActivity/(?P<act_id>[0-9]+)/$', views.updateActivity, name='updateActivity'),
    # ex: /cococloud/activity/5/
    url(r'^activity/(?P<act_id>[0-9]+)/$', views.activityDetail, name='activityDetail'),

    #------- Action (predicate) -------
    url(r'^actions/$', views.actions, name='actions'),

    #------- Subject/Object (URIRef) -----
    url(r'^nouns/$', views.nouns, name='nouns'),

    #------- Tags ----
    url(r'^tags/$', views.tags, name="tags"),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='tag'),
    url(r'^auth/(?P<u>.+)/(?P<p>.+)/$', views.auth, name='auth'),

    ]