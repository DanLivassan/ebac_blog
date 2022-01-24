from django.urls import path
from blog.views import PostView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
