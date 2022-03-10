from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse

from .models import Todo
from .forms import TodoForm


class IndexView(generic.ListView):
    model = Todo
    template_name = "index.html"

    form_class = TodoForm

    def get_queryset(self):
        todos = Todo.objects.order_by('-create_at')
        return todos


class TodoCreate(CreateView):
    model = Todo

    form_class = TodoForm

    def get_success_url(self):
        return reverse("try:index")