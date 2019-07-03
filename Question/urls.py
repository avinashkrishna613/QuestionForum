from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('asked/', views.askedp),
    path('logout/', views.logout_v),
    path('wanna.ask/', views.postques),
    path('answer/', views.answerp),
    path('search/', views.searchp),
    re_path(r'^paginate/(?P<slug>[0-9]{1})/$', views.listing),
    re_path(r'^val/(?P<slug>\d+)/$', views.hello),
]