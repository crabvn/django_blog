import requests
from .DataParser import DataParser
from django.conf import settings

class ContentfulRequest:
    def __init__(self):
        self.endpoint = settings.CONTENTFUL_API_HOST
        self.space = settings.CONTENTFUL_API_SPACE
        self.environment = settings.CONTENTFUL_API_ENVIRONMENT
        self.api_key = settings.CONTENTFUL_API_KEY
    
    def make_request(self, content_type, filters = {}, search_single = False):
        # Make request
        request_url = self.__generate_request_url(content_type, filters)
        response = requests.get(request_url)
        data = response.json()
        
        if (data['total'] == 0):
            return {
                'status' : 404,
                'message' : 'resource not found'
            }

        # Parse data into readable content instead of using contentful default response
        parser = DataParser(content_type, search_single)
        parser.set_data(data)
        parsed_data = parser.parse()

        return parsed_data

    def __get_default_filter(self):
        return {}

    def __generate_request_url(self, content_type, filters = {}):
        filter_text = ''
        for filter_item in filters:
            item = [
                '&fields.', 
                filter_item.get('field'),
                '[',
                filter_item.get('query'),
                ']',
                '=',
                filter_item.get('value')
            ]
            filter_text += ''.join(item)

        return ''.join([
            self.endpoint,
            'spaces/',
            self.space,
            '/environments/',
            self.environment,
            '/entries',
            '?',
            'content_type',
            '=',
            content_type,
            '&',
            'access_token',
            '=',
            self.api_key,
            filter_text
        ])
