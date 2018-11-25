from django.shortcuts import render
from .services.RequestService import ApiRequest

api_request = ApiRequest()

def index(request):
    indexPosts = api_request.get('blog')
    return render(request, 'pages/index.html', {
         'posts' : indexPosts
    })

def contact(request):
    return render(request, 'pages/contact.html')

def category(request, slug):
    data = api_request.get('category')
    return render(request, 'pages/category.html', {
         'category' : data
    })

def page(request, slug):
    search = [
         {
              'field' : 'slug',
              'value' : slug,
              'query' : 'match'
         }
    ]
    page = api_request.get('page', search, True)

    if(page.get('status') == 404):
         return render(request, 'pages/404.html')
    return render(request, 'pages/post.html', {
         'post' : page
    })

def post(request, slug):
    search = [
         {
              'field' : 'slug',
              'value' : slug,
              'query' : 'match'
         }
    ]
    post = api_request.get('blog', search, True)

    if(post.get('status') == 404):
         return render(request, 'pages/404.html')
    return render(request, 'pages/post.html', {
         'post' : post
    })
