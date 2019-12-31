from django.conf.urls import url
from . import views


app_name = 'main'
urlpatterns = [
    url(r'^$', views.showHome, name="showHome"),
    url(r'^clothes/$', views.showClothes, name="showClothes"),
    url(r'^collect/pazzo$', views.collectPazzo, name="collectPazzo"),
] 
