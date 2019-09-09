# About the repository
This is a simple blog built with django framework using content from API. We don't have admin pages.
* All the data will come from Contentful.com, Contentful provides you an application to create/manage your contents. Its super powerful for the simple blog.
* Available api source
Contenful. Read more at https://contentful.com

# How to start?
What you need to start?
- Python3
- Content API, such as contentful.com

## Clone the project
In your command line, run:
```
git clone git@github.com:crabvn/django_blog.git
```

## Settings Configuration
Go to settings.py add below lines
```
try:
    from .blog.blog_settings import *
except ImportError:
    pass
```

## Endpoint configurarion
Save `blog/blog_settings.py.dev` as `blog/blog_settings.py` then go to `blog/blog_settings.py` and change your setting endpoint. 
* CONTENTFUL_API_KEY: Your contentful API KEY: 
* CONTENTFUL_API_HOST: Your contentful api host, in my case my host is:`https://cdn.contentful.com/`
* CONTENTFUL_API_SPACE: Your contentful working space
* CONTENTFUL_API_ENVIRONMENT: Your contentful working environment, in my case I am using master environment so I put `master` to this setting.

## Start 
run `python3 manage.py runserver` then enter `http://127.0.0.1:8000/` to your browser

### Enjoy :)
