from django.urls import path
from . import views


urlpatterns = [
    path('', views.render_home, name='home'),
    path('count', views.count_words, name='counter'),
    path('about', views.render_about, name='about'),
]
