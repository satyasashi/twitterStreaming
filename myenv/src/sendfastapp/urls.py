from django.conf.urls import url
from tweetStream import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stream$', views.stream_query, name="stream_query")
]
