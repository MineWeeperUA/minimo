from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

from .models import *

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(
        help_text = "Наповніть статтю:)",
        label = "Наповнення статті",
        widget = CKEditorUploadingWidget()
        )
    class Meta:
        model = Article
        fields = '__all__'

class CommentInline(admin.TabularInline):
    extra = 1
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'id')
    inlines = [CommentInline]
    form = ArticleAdminForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')

admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)