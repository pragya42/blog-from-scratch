from django.shortcuts import render
from django.views.generic import ListView, DetailView 
#list would bring all of the blog posts , detail one but full details :| don't know if that makes sense query sets
from .models import Post
# Create your views here.
#def home(request):
#	return render(request,'home.html',{})
 
 #creating home view using class now
class HomeView(ListView):
	model = Post
	template_name = 'home.html'
  #coz we wanna use all the lists 


class ArticleDetailView(DetailView):
	model = Post
	template_name =  'article_details.html'
