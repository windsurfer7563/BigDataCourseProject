from django.conf.urls import url

from . import views

app_name = 'predict'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^make_predict/$', views.make_prediction, name='make_prediction'),
]
