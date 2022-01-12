from wsgidav.dav_provider import DAVNonCollection
import io
import random

class virtual_random_file_provider(DAVNonCollection):

    def __init__(self, path, environ, display_name=None, display_type=None):
        super().__init__(path, environ)
        self.name = "random.txt"
        self.content = str(random.random()*10)

    def support_etag(self):
        return False

    def get_display_name(self):
        return self.name

    def get_etag(self):
        return None

    def get_content_length(self):
        length=len(self.content)
        return length

    def get_content_type(self):
        return "text/plain"

    def get_content(self):
        print("content is {0}", self.content)
        old_content = io.BytesIO(self.content.encode("utf-8"))
        self.content = str(random.random()*10)
        return old_content