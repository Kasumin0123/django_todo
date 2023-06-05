from django.urls import path
from .views import Index, List, Detail, Create, Update, Delete, ListIndex, CreateList, DeleteList

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('index/', List.as_view(), name="todolist"),
    path('detail/<pk>', Detail.as_view(), name="tododetail"),
    path('create/', Create.as_view(), name="todocreate"),
    path('edit/<pk>', Update.as_view(), name="todoupdate"),
    path('delete/<pk>', Delete.as_view(), name="tododelete"),
    path('list/', ListIndex.as_view(), name="listindex"),
    path('newlist/', CreateList.as_view(), name="listcreate"),
    path('deletelist/<pk>', DeleteList.as_view(), name="listdelete"),
]
