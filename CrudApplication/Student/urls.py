from django.urls import path
from Student import views as StudentViews

urlpatterns = [
    path('', StudentViews.index, name='index'),
    path('insert', StudentViews.insert, name='insert'),
    path('update/<stu_id>', StudentViews.update, name='update'),
    path('delete/<stu_id>', StudentViews.delete, name='delete'),
]