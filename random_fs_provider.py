from wsgidav import dav_provider
from virtual_random_file import virtual_random_file_provider
from virtual_random_folder import virtual_random_folder

class RandomFSProvider(dav_provider.DAVProvider):
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