from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Author, Article
from .services import Services

def index(request):
  template = loader.get_template('references/index.html')
  return HttpResponse(template.render({}, request))

def authors(request):
  # We sure don't want to do this every time! This hits the 3rd party API when it's
  # called and grabs the default-number of records. A real implementation wouldn't do this;
  # we would pull the data separately, maybe in a regular job, and just load it from our db here
  s = Services
  s.run_query(s)
  template = loader.get_template('references/authors.html')
  return HttpResponse(template.render({'authors': Author.objects.all()}, request))

def latest(request):
  s = Services
  s.run_query(s)
  template = loader.get_template('references/latest.html')
  return HttpResponse(template.render({'articles': Article.get_latest()}, request))
