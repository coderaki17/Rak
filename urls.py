from django.urls import path
from .views import Homeview,ArticleDetailView

urlpatterns = [
    path('', Homeview.as_view(), name="Home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),

]

