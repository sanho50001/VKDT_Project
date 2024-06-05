from django.urls import path
from .views import (
    MainView,
    post
)

app_name = "VK"

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('post/', post, name='post'),

    # path("main/<int:pk>/", NewsDetailsView.as_view(), name="news_detail"),
]
