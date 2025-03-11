from django.urls import path
from product import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    # path('about', views.about, name='about'),
    path("about/", views.ContactView.as_view(), name='about'),
]
