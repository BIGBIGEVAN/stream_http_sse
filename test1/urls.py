from django.urls import path

from .views import IndexView, PostStreamView

app_name = 'test1'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('stream/', PostStreamView.as_view(), name='stream'),
]