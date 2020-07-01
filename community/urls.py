from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.CommunityLV.as_view(), name='index'),
    path('<int:pk>/', views.CommunityDV.as_view(), name='detail'),
    path('add/', views.CommunityCreateView.as_view(), name='add', ),
    path('change/', views.CommunityChangeLV.as_view(), name='change', ),
    path('<int:pk>/update/', views.CommunityUpdateView.as_view(), name='update', ),
    path('<int:pk>/delete/', views.CommunityDeleteView.as_view(), name='delete', ),
]
