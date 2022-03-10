from . import views

from django.urls import include, path


app_name = 'try'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.TodoCreate.as_view(), name='create'),
]
