from django.test import TestCase

from .models import Article, Author
from .services import Services


class ReferenceServiceTests(TestCase):
  def test_build_search_query(self):
    s = Services
    r = s.build_query(s, "foo")
    self.assertEqual(r, "http://export.arxiv.org/api/query?search_query=foo")
  
  # this method hits an actual API. In a real-world scenario,
  # I would build a mock to return a controlled, predictable
  # response when the method attempts to ping the API.
  
  # this also means I'm not actually testing the content,
  # since I can't control the content returning from a 3rd
  # party API

  def test_get_articles_returns_valid_data(self):
    s = Services
    ret = s.get_article_data(s)

    self.assertGreater(len(ret), 0)

  # would likely be a serializer in a real-world scenario!
  def test_data_parser(self):
    s = Services
    auth1 = "Banana Fanna McGee"
    auth2 = "Cool Kid Joe"
    auth3 = "Less Cool Kid Joey"
    art1 = "An Article"
    art2 = "Another Article"
    art3 = "omg a THIRD ARTICLE"
    art4 = "Article 4? Can't Be!"
    date = "2003-07-07T13:46:39-04:00"
    
    parseable_data = [
      {
        "name": art1,
        "author": auth1,
        "publication_date": date
      },
      {
        "name": art2,
        "author": auth2,
        "publication_date": date
      }
    ]

    start_len_auth = len(Author.objects.all())
    start_len_art = len(Article.objects.all())
    # technically unnecessary...but I like to see numbers working
    self.assertEqual(start_len_auth, 0)
    self.assertEqual(start_len_art, 0)

    data = s.parse_data(s, parseable_data)

    self.assertEqual(len(data), 2)

    mid_len_auth = len(Author.objects.all())
    mid_len_art = len(Article.objects.all())

    # it adds new authors when appropriate
    self.assertEqual(mid_len_auth, start_len_auth + 2)
    self.assertEqual(mid_len_art, start_len_art + 2)

    # it only adds new authors and does not duplicate the same author twice

    semi_parseable = [
      {
        "name": art1,
        "author": auth1,
        "publication_date": date
      },
      {
        "name": art3,
        "author": auth3,
        "publication_date": date
      }
    ]

    s.parse_data(s, semi_parseable)

    third_len_auth = len(Author.objects.all())
    third_len_art = len(Article.objects.all())

    self.assertEqual(third_len_auth, mid_len_auth + 1)
    self.assertEqual(third_len_art, mid_len_art + 1)

    # a repeat author with a new article
    parseable_repeat_author = [
      {
        "name": art4,
        "author": auth1,
        "publication_date": date
      }
    ]


    s.parse_data(s, parseable_repeat_author)

    last_len_auth = len(Author.objects.all())
    last_len_art = len(Article.objects.all())

    self.assertEqual(last_len_auth, third_len_auth)
    self.assertEqual(last_len_art, third_len_art + 1)

  # again, in the real world, would test with a mock so I'm not hitting a live API
  def test_run_query(self):
    s = Services

    start_len_auth = len(Author.objects.all())
    start_len_art = len(Article.objects.all())
    # technically unnecessary...but I like to see numbers working
    self.assertEqual(start_len_auth, 0)
    self.assertEqual(start_len_art, 0)

    s.run_query(s)

    post_query_auth = Author.objects.all()
    post_query_art = Article.objects.all()

    # would be more specific if I had a mock of data to test with!
    self.assertGreater(len(post_query_art), start_len_art)
    self.assertGreater(len(post_query_auth), start_len_auth)

class ReferenceModelArticleTests(TestCase):
  def test_get_latest(self):
    s = Services

    # lots of junk data here! would love a factory to build test data :)
    wordbank = [
      "foo", "bar", "baz", "banana", "potato", "query", "falafel", "greyhound", "eleven", "small black cat", "lampshade", "violet"
    ]

    old_date = "2003-07-07T13:46:39-04:00"
    recent_date = "2013-07-07T13:46:39-04:00"

    parseable_data = []
    name_str = "hopefully, this won't show"

    for word in wordbank:

      parseable_data.append({"name": word, "author": word, "publication_date": recent_date})

    parseable_data.append({"name": name_str, "author": "an autor", "publication_date": old_date})

    s.parse_data(s, parseable_data)

    old_article = Article.objects.filter(name=name_str)[0]
    self.assertEqual(old_article.author.name, "an autor")

    latest = Article.get_latest()

    self.assertEqual(len(latest), 10)

    all_articles = Article.objects.all()

    self.assertIn(old_article, all_articles)
    self.assertNotIn(old_article, latest)

