from django.urls import path
from blog.views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
]
