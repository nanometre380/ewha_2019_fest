"""ewhafest2019 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name = "home"), #메인 인덱스 패스
    path('import_fest/', home.views.import_fest, name = "import"), #csv import 패스
    path('home/first/', home.views.first, name = "first"), #첫날
    path('home/second/', home.views.second, name = "second"), #둘째
    path('home/third/', home.views.third, name = "third"), #셋째
    path('home/search/', home.views.search, name = "search"), #검색
    path('home/sold_out/', home.views.sold_out, name = "sold_out"), #sold_out
    path('home/board/', home.views.board, name = "board"),
    path('home/comment_write/', home.views.comment_write, name="comment_write"),
]
