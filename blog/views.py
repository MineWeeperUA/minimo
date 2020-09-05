from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import *
from .forms import CommentForm


class indexView (View):
	def get (self, request):
		latest_article = Article.objects.first()
		top_articles = Article.objects.all()[1:5]
		bottom_articles = Article.objects.all()[5:]
		amount_of_articles = Article.objects.count()
		return render (
			request, 
			'index.html', 
			context = {
				"latest_article" : latest_article,
				"top_articles" : top_articles,
				"bottom_articles" : bottom_articles,
				"amount_of_articles" : amount_of_articles
				}
			)

class articleView (DetailView):
	model = Article
	slug_field = 'url'
	template_name = 'article.html'

class addReactionArticleView (View):
	def get (self, request, pk, slug):	
		article = Article.objects.get(id = pk)
		if slug == "like":
			article.likes += 1
		elif slug == "dislike":
			article.dislikes += 1
		article.save()
		return redirect(article.get_absolute_url())

class addReactionCommentView (View):
	def get (self, request, num, pk, slug):	
		comment = Comment.objects.get(id = pk)
		article = Article.objects.get(id = num)
		if slug == "like":
			comment.likes += 1
		elif slug == "dislike":
			comment.dislikes += 1
		comment.save()
		return redirect(article.get_absolute_url())

class addComment (View):
	def post (self, request, pk):
		form = CommentForm(request.POST)
		article = Article.objects.get(id = pk)
		if form.is_valid():
			form = form.save(commit = False)
			if request.POST.get("parent", None):
				form.parent_id = int(request.POST.get("parent"))
			form.article = article
			form.save()
		return redirect(article.get_absolute_url())
		
class termsAndConditions (View):
	def get (self, request):
		return render (
			request, 
			'terms_and_conditions.html'
			)

class privacy (View):
	def get (self, request):
		return render (
			request, 
			'privacy.html'
			)

class category (ListView):
	pass
		