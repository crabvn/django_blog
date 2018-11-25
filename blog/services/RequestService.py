import requests
from django.conf import settings
from .contentful.Request import ContentfulRequest

class ApiRequest:
    def __init__(self):
        if (settings.API_SERVICE == 'contentful'):
            self.api_service = ContentfulRequest()
    
    def get(self, content_type, filters = {}, search_single = False):
        return self.api_service.make_request(content_type, filters, search_single)
