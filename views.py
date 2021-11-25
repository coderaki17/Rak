from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post


#def home(request):
 #   return render(request, 'home.html',{})


class Homeview(ListView):
    model = post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = post 
    template_name = 'article_details.html'
