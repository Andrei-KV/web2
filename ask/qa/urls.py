from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^', views.head, name='head'),
    re_path(r'^login/', views.test, name='test'),
    re_path(r'^signup/', views.test, name='test'),
    re_path(r'^question/\d+', views.test, name='test'),
    re_path(r'^ask/', views.test, name='test'),
    re_path(r'^popular/', views.test, name='test'),
    re_path(r'^new/', views.test, name='test'),
]