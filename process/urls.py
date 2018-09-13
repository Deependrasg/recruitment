from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<user>\d+)/questions/$', views.questions, name='questions'),
    url(r'^ratings/$', views.ratings, name='ratings'),
    url(r'^(?P<user>\d+)/result/$', views.result, name='result'),
    url(r'^results/$', views.result_index, name='result_index'),
]