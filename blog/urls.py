from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.posts_by_category, name='posts_by_category'),
    path('about-me', views.about_me, name='about_me'),
    path('contact-me', views.contact, name='contact'),
]
