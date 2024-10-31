from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class UserListView(ListView):
    template_name = "userlist.html"
    model = User
    context_object_name = "users"

class UserAddView(CreateView):
    template_name = "useradd.html"
    model = User
    fields = ['full_name', 'age', 'email', 'phone', 'image']
    success_url = reverse_lazy("userlist")

class UserUpdateView(UpdateView):
    template_name = "userupd.html"
    model = User
    fields = ['full_name', 'age', 'email', 'phone', 'image']
    success_url = reverse_lazy("userlist")

class UserDeleteView(DeleteView):
    template_name = "userdel.html"
    model = User
    success_url = reverse_lazy("userlist")


class RoomListView(ListView):
    template_name = "roomlist.html"
    model = Room
    context_object_name = "rooms"

class RoomAddView(CreateView):
    template_name = "roomadd.html"
    model = Room
    fields = ['number', 'rooms', 'category', 'image']
    success_url = reverse_lazy("roomlist")

class RoomUpdateView(UpdateView):
    template_name = "roomupd.html"
    model = Room
    fields = ['number', 'rooms', 'category', 'image']
    success_url = reverse_lazy("roomlist")

class RoomDeleteView(DeleteView):
    template_name = "roomdel.html"
    model = Room
    success_url = reverse_lazy("roomlist")

class BookListView(ListView):
    template_name = "booklist.html"
    model = Booking
    context_object_name = "books"

class BookAddView(CreateView):
    template_name = "bookadd.html"
    model = Booking
    fields = ['user', 'room', 'duration']
    success_url = reverse_lazy("booklist")

class BookUpdateView(UpdateView):
    template_name = "bookupd.html"
    model = Booking
    fields = ['user', 'room', 'duration']
    success_url = reverse_lazy("booklist")

class BookDeleteView(DeleteView):
    template_name = "bookdel.html"
    model = Booking
    success_url = reverse_lazy("booklist")