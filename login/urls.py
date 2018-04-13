from django.conf.urls import url
from django.views.generic import TemplateView



from . import views

app_name = 'login'


urlpatterns = [
    # url(r'^$', views.IndexView.as_view()),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
 
    url(r'^$',TemplateView.as_view(template_name = 'login/login.html')),
    url(r'^login/', views.login, name = 'login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^$',TemplateView.as_view(template_name = 'login/home.html'),name="loggedin"),

    
]

