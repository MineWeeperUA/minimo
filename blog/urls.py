from django.urls import path

from . import views

urlpatterns = [
	path('', views.indexView.as_view(), name='index'),
	path('article/<slug:slug>', views.articleView.as_view(), name='article'),
	path('comment/addreaction/<slug:slug>/<int:num>/<int:pk>', views.addReactionCommentView.as_view(), name='addreactioncomment'),
	path('article/addreaction/<slug:slug>/<int:pk>', views.addReactionArticleView.as_view(), name='addreactionarticle'),
	path('comment/<int:pk>', views.addComment.as_view(), name='add_comment'),
	path('terms-and-conditions', views.termsAndConditions.as_view(), name='terms_and_conditions'),
	path('privacy', views.privacy.as_view(), name='privacy'),
	path('category/<slug:slug>', views.category.as_view(), name='category')
]