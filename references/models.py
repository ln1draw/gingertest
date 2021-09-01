from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Article(models.Model):
  name = models.CharField(max_length=200)
  publication_date = models.DateTimeField('date published')
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  @classmethod
  def get_latest(cls):
    ret = Article.objects.order_by('-publication_date')[:10]
    return ret