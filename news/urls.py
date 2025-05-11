from django.urls import path
# Импортируем созданные нами представления
from news.views import NewsList, NewDetail, NewCreate, NewSearch, NewUpdate, NewDelete


urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>/', NewDetail.as_view(), name='new_detail'),
   path('search/', NewSearch.as_view()),

   path('create/', NewCreate.as_view(), name='news_create'),
   path('articles/create', NewCreate.as_view(), name='articles_create'),
   path('<int:pk>/edit/', NewUpdate.as_view(), name='news_edit'),
   path('articles/<int:pk>/edit/', NewUpdate.as_view(), name='articles_edit'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', NewDelete.as_view(), name='articles_delete')

]