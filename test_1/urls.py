"""
URL configuration for test_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# test_1 项目 路由 -> 子路由 or 路由 -> 视图
"""
匹配成功则跳过下面的匹配
全都匹配不成功则返回404
"""
urlpatterns = [
    path('', include('book.urls'), name="home"),
    path('admin/', admin.site.urls),

]
