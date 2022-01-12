from wsgidav.dav_provider import DAVCollection
import wsgidav.samples.dav_provider_tools as provider_tools

class virtual_random_folder(DAVCollection):
    def __init__(self, path, environ, file):
        DAVCollection.__init__(self, path, environ)
        self.file = file

    def get_member_names(self):
        return ["random.txt".encode("utf8")]

    def get_member(self, path):
        return self.file