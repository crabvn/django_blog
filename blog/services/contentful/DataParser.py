from rich_text_renderer import RichTextRenderer

class DataParser:
    def __init__(self, content_type, single_entry = False):
        self.content_type = content_type
        self.data_parsed = []
        self.renderer = RichTextRenderer()
        self.single_entry = single_entry

    def set_data(self, data):
        self.data = data

    def parse(self):
        self.__parse_default()
        if (self.single_entry == True):
            return self.data_parsed[0]
        else:
            return self.data_parsed
    
    def __parse_default(self):
        items = self.data['items']
        for item in items:
            parsed_item = item.get('fields')
            self.data_parsed.append(self.__parse_document_field(parsed_item))

    def __parse_document_field(self, item):
        parsed_item = {}
        for key, value in item.items():
            if(isinstance(value, dict)):
                #is not None means has nodeType value
                if(value.get('nodeType') and value.get('nodeType') == 'document'):
                    list_content = self.renderer.render(value)
                    value = list_content
            parsed_item.update({key : value})

        return parsed_item
