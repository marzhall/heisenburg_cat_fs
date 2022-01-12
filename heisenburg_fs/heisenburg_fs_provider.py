from wsgidav import dav_provider
from heisenburg_fs.heisenburg_cat_box import heisenburg_cat_box
from heisenburg_fs.heisenburg_folder import heisenburg_folder

class HeisenburgFSProvider(dav_provider.DAVProvider):
    """
    This is the top-level "app" of the heisenburgFS server.
    All requests to the server go through this endpoint,
    and it's registered to the cheroot web server we're
    hosting ourselves on at a given path, in our case the
    `/` directory of the site.

    When the cheroot web server is hit at then endpoint
    we've registered to, its "get_resource_inst" method is
    called, along with a path to a resource that the user
    is requesting, e.g. "/heisenburg.txt". The server then
    returns a wsgidav object for that given path.
    """ 
    def __init__(self):
        super().__init__()
        self.heisenburg_file = None
        self.heisenburg_folder = None

    def get_resource_inst(self, path, environ):
        """
        When a user hits the web server on which we're hosted asking for a file,
        the webserver (in our case, cheroot) then calls this method with the path
        the user is requesting.

        Here, we've hardcoded results for two paths: "/", which returns a directory
        object that will list its contents as our virtual `the_cat_box.txt` file;
        and "/the_cat_box.txt", which returns an object that, when read, will return
        whether Heisenburg's cat is dead or alive.
        """
        if self.heisenburg_file == None:
            self.heisenburg_file = heisenburg_cat_box("/the_cat_box.txt", environ, display_name="the_cat_box.txt")
        if self.heisenburg_folder == None:
            self.heisenburg_folder = heisenburg_folder("/", environ, self.heisenburg_file)
        if path == "/":
            return self.heisenburg_folder
        if path == "/the_cat_box.txt":
            return self.heisenburg_file
        else:
            raise Exception(str.format("File {0} does not exist.", path))