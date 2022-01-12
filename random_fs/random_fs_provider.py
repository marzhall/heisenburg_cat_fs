from wsgidav import dav_provider
from random_fs.virtual_random_file import virtual_random_file_provider
from random_fs.virtual_random_folder import virtual_random_folder

class RandomFSProvider(dav_provider.DAVProvider):
    """
    This is the top-level "app" of the randomFS server.
    All requests to the server go through this endpoint,
    and it's registered to the cheroot web server we're
    hosting ourselves on at a given path, in our case the
    `/` directory of the site.

    When the cheroot web server is hit at then endpoint
    we've registered to, its "get_resource_inst" method is
    called, along with a path to a resource that the user
    is requesting, e.g. "/random.txt". The server then
    returns a wsgidav object for that given path.
    """ 
    def __init__(self):
        super().__init__()
        self.random_file = None
        self.random_folder = None

    def get_resource_inst(self, path, environ):
        if self.random_file == None:
            self.random_file = virtual_random_file_provider("/random.txt", environ, display_name="random.txt")
        if self.random_folder == None:
            self.random_folder = virtual_random_folder("/", environ, self.random_file)
        if path == "/":
            return self.random_folder
        if path == "/random.txt":
            return self.random_file
        else:
            raise Exception(str.format("File {0} does not exist.", path))