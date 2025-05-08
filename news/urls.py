from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewDetail

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>/', NewDetail.as_view(), name='new_detail'),
]