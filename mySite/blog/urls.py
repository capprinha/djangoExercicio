from django.urls import path

from .views import PostView

from .views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home')
]