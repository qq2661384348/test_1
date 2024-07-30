from django.urls import path
from book.views import *

# book 路由 -> 视图
urlpatterns = [
    path('', index),
    path('testApi/<int:id_1>/<int:id_2>', test_api),
    path('favicon.ico', favicon)

]
