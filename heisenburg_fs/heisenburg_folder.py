from wsgidav.dav_provider import DAVCollection
import wsgidav.samples.dav_provider_tools as provider_tools

class heisenburg_folder(DAVCollection):
    """ 
    This object holds other objects inside it,
    so it's effectively a directory/folder.
    This instance is hardcoded to return just
    one file, our the_cat_box.txt file.
    """
    def __init__(self, path, environ, file):
        DAVCollection.__init__(self, path, environ)
        self.file = file

    def get_member_names(self):
        return ["the_cat_box.txt".encode("utf8")]

    def get_member(self, path):
        return self.file