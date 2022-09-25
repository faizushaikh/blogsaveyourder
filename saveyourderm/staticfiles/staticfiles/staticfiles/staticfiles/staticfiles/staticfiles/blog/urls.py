from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, post,category,about



urlpatterns = [
    path('',home,name='home'),
    path('blog/<slug:post_id>',post),
    path('category/<slug:url>',category),
    path('about-us',about)
]
