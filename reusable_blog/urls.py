from django.conf.urls import url

import views


urlpatterns = [
    url(r'^/$', views.post_list),
    url(r'^/(?P<id>\d+)/$', views.post_detail),
    url(r'^/topfive', views.post_five),
    url(r'^post/new/$', views.new_post, name='new post'),
    url(r'^/(?P<id>\d+)/edit$', views.edit_post),
]