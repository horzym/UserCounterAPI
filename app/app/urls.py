from django.urls import path
from UserCounter.views import UserCounter


urlpatterns = [
    path(r'api/user/<int:id>/counter',
         UserCounter.as_view(), name='user-counter'),
]
