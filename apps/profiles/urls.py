from django.urls import path

from .views import (
    get_all_agents, 
    top_agent_list, 
    GetProfileAPIView, 
    UpdateProfileAPIView
)

urlpatterns = [
    path('me/', GetProfileAPIView.as_view(), name='get_profile'),
    path("update/<str:username>", UpdateProfileAPIView.as_view(), name="update_profile"),
    path('agents/all/', get_all_agents, name='all-agents'),
    path('top-agents/all/', top_agent_list, name='top-agents')
]