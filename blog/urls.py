from django.urls import path
from . import views
urlpatterns = [
    path("", views.post_list, name= 'post_list'),
    path('ja/', views.ja_view, name='ja'),
]
