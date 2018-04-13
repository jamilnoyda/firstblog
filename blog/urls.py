from django.conf.urls import url



from . import views


app_name='blog'

urlpatterns = [
    #url(r'^$', views.post, name='post'),
    url('^blog/$', views.BlogListView.as_view(), name='home'),
    url('^blog/(?P<pk>[0-9]+)/detail/$',views.BlogDetailView.as_view(), name='post_detail')



]
 