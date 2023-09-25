from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from django.views.generic.edit import CreateView
class ArticleListView(ListView):
    model = models.Aricle
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = models.Aricle
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = models.Aricle
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = models.Aricle
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = models.Aricle
    template_name = 'article_new.html'
    fields = ['title', 'body', 'author']