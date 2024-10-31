from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name = "home"),
    path("userlist/", UserListView.as_view(), name = "userlist"),
    path("useradd/", UserAddView.as_view(), name = "useradd"),
    path("userupd/<int:pk>/", UserUpdateView.as_view(), name = "userupd"),
    path("userdel/<int:pk>/", UserDeleteView.as_view(), name = "userdel"),
    path("roomlist/", RoomListView.as_view(), name = "roomlist"),
    path("roomadd/", RoomAddView.as_view(), name = "roomadd"),
    path("roomupd/<int:pk>/", RoomUpdateView.as_view(), name = "roomupd"),
    path("roomdel/<int:pk>/", RoomDeleteView.as_view(), name = "roomdel"),
    path("booklist/", BookListView.as_view(), name = "booklist"),
    path("bookadd/", BookAddView.as_view(), name = "bookadd"),
    path("bookupd/<int:pk>/", BookUpdateView.as_view(), name = "bookupd"),
    path("bookdel/<int:pk>/", BookDeleteView.as_view(), name = "bookdel"),
]