from core.api_client import ApiClient
from global_constant import url_data


class ContentBuilder:
    api_client = ApiClient()


    def get_api_links(self):
        links = []
        for entry in url_data:
            url, field_name = entry
            link = self.api_client.get_link(url, field_name)
            links.append(link)
        return links

    def create_message_content(self, links):
        message = ""
        for link in links:
            message += link + "\r\n"
        return message
