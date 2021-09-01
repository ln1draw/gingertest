import feedparser
import datetime

from .models import Article, Author

class Services():
  # query has settable sortBy and sortOrder params 

  def build_query(self, search_query):
    # possible this will be updated if the query is changed in the future
    url_root = "http://export.arxiv.org/api/query?search_query="
    return url_root + search_query

  def get_article_data(self):
    ret = []

    params = "all:psychiatry+OR+all:therapy+OR+all:data+science+OR+all:machine+learning"

    feed = feedparser.parse(self.build_query(self, params))
    
    # realistically this could be refactored to mesh better and less 
    # repetitively with parse_data
    for key in feed.entries:
      ret.append({
        'name': key.title,
        'publication_date': key.published, #not currently doing anything with "updated"
        'author': key.author
      })

    return ret

  # would likely be the work of a serializer in a real-world scenario
  def parse_data(self, data):
    ret = []
    for article in data:

      date = article['publication_date']
      
      # this data use is a bit sloppy! I don't like this author lookup. Lots of potential for dirty data here
      # this also doesn't account for articles with multiple authors
      
      author = Author.objects.get_or_create(name=article["author"])[0]
      author.save()
      
      article = Article.objects.get_or_create(author__id=author.id,name=article["name"],defaults={'publication_date': date, 'author': author})[0]
      article.save()
      
      ret.append({"author": author, "article": article})
    
    return ret

  def run_query(self):
    data = self.parse_data(self, self.get_article_data(self))
    return data
