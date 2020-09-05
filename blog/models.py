from django.db import models
from django.utils import timezone
from django.urls import reverse
import random


class Language (models.Model):
    name = models.CharField (
        max_length = 200,
        help_text = "Введіть мову написання статті"
        )
    
    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = "Мова"
        verbose_name_plural = "Мови"

class Category (models.Model):
    name = models.CharField (
        max_length = 200,
        help_text = "Введіть назву категорії"
        )
    language = models.ForeignKey (
        Language,
        on_delete = models.SET_NULL,
        null = True
        )

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Article (models.Model):
    title = models.CharField (
    	"Назва статті",
  		max_length = 250,
        help_text = "Введіть назву статті"
        )
    main_image = models.ImageField (
        'Титульне зображення',
        upload_to ='title_images'
        ) 
    author = models.CharField (
    	"Автор статті",
  		max_length = 250,
        help_text = "Введіть назву статті"
        )
    pub_date = models.DateTimeField (
    	"Дата публікації",
		help_text = "Введіть дату публікації"
    	)
    content = models.TextField (
    	"Наповнення статті",
    	help_text = "Наповніть статтю:)"
    	)
    text_on_main = models.TextField (
        "Текст статті на головній сторінці",
        help_text = "Введіть текст статті, що відобразиться на головній сторінці"
        )
    likes = models.IntegerField (
    	"Кількість лайків",
        default = 0
    	)
    dislikes = models.IntegerField (
    	"Кількість дизлайків",
        default = 0
    	)
    category = models.ManyToManyField (
    	Category,
    	help_text="Оберіть категорію"
    	)
    language = models.ForeignKey (
    	Language,
    	on_delete = models.SET_NULL, 
    	null = True
    	)
    url = models.SlugField(
        max_length = 130,
        unique = True
        )
    def __str__ (self):
    	return self.title

    def get_absolute_url (self):
    	return reverse('article', kwargs={'slug' : self.url})
    def get_comments (self):
        return self.comment_set.filter(parent__isnull=True)
    def get_related_articles (self):
        related_article_1_id = random.randint(1, Article.objects.count())   
        while related_article_1_id == self.id:
            related_article_1_id = random.randint(1, Article.objects.count())
        related_article_2_id = random.randint(1, Article.objects.count())
        while related_article_2_id == related_article_1_id or related_article_2_id == self.id:
            related_article_2_id = random.randint(1, Article.objects.count())
        related_article_3_id = random.randint(1, Article.objects.count())
        while related_article_3_id == related_article_2_id or related_article_3_id == related_article_1_id or related_article_3_id == self.id:
            related_article_3_id = random.randint(1, Article.objects.count())
        related_article_1 = Article.objects.get(
            id = related_article_1_id
            )
        related_article_2 = Article.objects.get(
            id = related_article_2_id
            )
        related_article_3 = Article.objects.get(
            id = related_article_3_id
            )
        related_articles = [related_article_1, related_article_2, related_article_3]

        return related_articles

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ['-pub_date', 'author']

class Comment (models.Model):
    article = models.ForeignKey (
        Article, 
        on_delete = models.CASCADE
        )
    author = models.CharField (
        "Автор коментаря",
        max_length = 250,
        help_text = "Введіть ім'я автора коментаря"
        )
    text = models.TextField (
        "Текст коментаря",
        help_text = "Введіть текст статті"
        )
    parent = models.ForeignKey (
        'self',
        verbose_name = "Предок",
        on_delete = models.SET_NULL,
        blank = True,
        null = True
        )
    pub_date = models.DateTimeField (
        "Дата публікації",
        help_text = "Введіть дату публікації",
        default = timezone.now
        )
    likes = models.IntegerField (
        "Кількість лайків",
        default = 0
        )
    dislikes = models.IntegerField (
        "Кількість дизлайків",
        default = 0
        )

    def __str__ (self):
        return self.author

    class Meta:
        verbose_name = "Кометар"
        verbose_name_plural = "Коментарі"