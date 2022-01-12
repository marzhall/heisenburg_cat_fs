from wsgidav.dav_provider import DAVNonCollection
import io
import random

class heisenburg_cat_box(DAVNonCollection):
    """
    This class is the equivalent of a file.
    When a user opens the node either in the web
    interface or in a mounted driver, they see the
    contents returned from get_content.
    
    In our case, get_content returns whether
    Heisenburg's cat is alive or dead.
    """

    def __init__(self, path, environ, display_name=None, display_type=None):
        super().__init__(path, environ)
        self.name = "the_cat_box.txt"
        self.dead_or_alive = "the cat is dead" if random.random()*10 > 5 else "the cat is alive"

    def support_etag(self):
        return False

    def get_display_name(self):
        return self.name

    def get_etag(self):
        return None

    def get_content_length(self):
        length=len(self.dead_or_alive)
        return length

    def get_content_type(self):
        return "text/plain"

    def get_content(self):
        print("Current status is:", self.dead_or_alive)
        old_state = io.BytesIO(self.dead_or_alive.encode("utf-8"))
        self.dead_or_alive = "the cat is dead" if random.random()*10 > 5 else "the cat is alive"
        return old_state