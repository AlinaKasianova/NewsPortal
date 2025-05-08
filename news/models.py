from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        # Рассчитываем рейтинг автора
        articles_rating = sum(post.rating * 3 for post in Post.objects.filter(author=self))
        comments_rating = sum(comment.rating for comment in Comment.objects.filter(user=self.user))
        comments_to_articles_rating = sum(comment.rating for post in Post.objects.filter(author=self) for comment in
                                          Comment.objects.filter(post=post))

        # Общий рейтинг
        self.rating = articles_rating + comments_rating + comments_to_articles_rating
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    news = " NW"
    articles = "AR"
    POST_TYPES = [(news, "новость"), (articles, "статья")]

    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    post_type = models.CharField(choices=POST_TYPES, max_length=3, default=news)
    date_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title.capitalize()

    def like(self):
        """ Увеличивает рейтинг поста на 1. """
        self.rating += 1
        self.save()

    def dislike(self):
        """ Уменьшает рейтинг поста на 1. """
        self.rating -= 1
        self.save()

    def preview(self):
        """ Возвращает предварительный просмотр текста поста. """
        return self.text[:124] + '...' if len(self.text) > 124 else self.text


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    date_at = models.DateTimeField(auto_now_add=True)

    def like(self):
        """ Увеличивает рейтинг комментария на 1. """
        self.rating += 1
        self.save()

    def dislike(self):
        """ Уменьшает рейтинг комментария на 1. """
        self.rating -= 1
        self.save()
