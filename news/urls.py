from django.urls import path
from news import views
from .views import *

urlpatterns=[
    path("",views.home,name='home'),
    path("new",views.new,name='new'),
    path("new1",views.new1,name='new1'),
    path('detail/<int:id>',views.detail,name='detail'),
    path("search",views.search,name='search'),
    path('remove/<int:id>/',views.delete,name='remove'),

]
