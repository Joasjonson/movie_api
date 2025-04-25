from django.urls import path
from actors.views import ActorListCreateView, ActorDetailView

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='actor_list_create_view'),  
    path('actors/<int:pk>/', ActorDetailView.as_view(), name='actor_detail_view'),
]