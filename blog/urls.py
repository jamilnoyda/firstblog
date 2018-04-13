from django.conf.urls import url



from . import views


app_name='blog'

urlpatterns = [
    #url(r'^$', views.post, name='post'),
    url('^blog/$', views.BlogListView.as_view(), name='home'),
    url('^blog/(?P<pk>[0-9]+)/detail/',views.BlogDetailView.as_view(), name='post_detail'),
    url(r'^blog/new/$', views.post_new, name='post_new'),
    url(r'^blog/(?P<pk>[0-9]+)/update/', views.PostUpdate.as_view(), name='post_update'),
    url(r'^blog/(?P<pk>\d+)/detele/', views.PostDelete.as_view(), name='post_delete'),
    #url(r'^blog/(?P<pk>[0-9]+)/detele/', views.PostDelete.as_view(), name='post_delete'),






]
 