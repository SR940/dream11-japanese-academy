from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('jlpt-info/', views.jlpt_info_view, name='jlpt_info'),
    path('services/', views.services_view, name='services'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]

