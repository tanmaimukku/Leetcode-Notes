class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def read_content(self):
        return self.content

    def write_content(self, new_content):
        self.content = new_content

    def append_content(self, additional_content):
        self.content += additional_content

    def get_size(self):
        return len(self.content)


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

    def add_file(self, file_name, content=""):
        if file_name in self.files:
            raise ValueError(f"File '{file_name}' already exists in directory '{self.name}'.")
        self.files[file_name] = File(file_name, content)

    def get_or_create_file(self, file_name):
        if file_name not in self.files:
            self.files[file_name] = File(file_name)
        return self.files[file_name]

    def remove_file(self, file_name):
        if file_name not in self.files:
            raise ValueError(f"File '{file_name}' does not exist in directory '{self.name}'.")
        del self.files[file_name]

    def add_directory(self, directory_name):
        if directory_name not in self.subdirectories:
            self.subdirectories[directory_name] = Directory(directory_name)
        return self.subdirectories[directory_name]

    def remove_directory(self, directory_name):
        if directory_name not in self.subdirectories:
            raise ValueError(f"Directory '{directory_name}' does not exist in directory '{self.name}'.")
        del self.subdirectories[directory_name]

    def list_contents(self):
        return sorted(list(self.files.keys()) + list(self.subdirectories.keys()))


class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def ls(self, path):
        node = self._navigate_to_node(path)
        if isinstance(node, File):
            return [node.name]
        return node.list_contents()

    def mkdir(self, path):
        self._navigate_and_create_directories(path)

    def add_content_to_file(self, file_path, content):
        directory_path, file_name = file_path.rsplit("/", 1)
        directory = self._navigate_and_create_directories(directory_path)
        file = directory.get_or_create_file(file_name)
        file.append_content(content)

    def read_content_from_file(self, file_path):
        directory_path, file_name = file_path.rsplit("/", 1)
        directory = self._navigate_to_directory(directory_path)
        if file_name not in directory.files:
            raise ValueError(f"File '{file_name}' does not exist.")
        return directory.files[file_name].read_content()

    def search_by_size(self, size, current_directory=None, path=""):
        if current_directory is None:
            current_directory = self.root

        result = []
        for file_name, file in current_directory.files.items():
            if file.get_size() < size:
                result.append(f"{path}/{file_name}")

        for sub_dir_name, sub_dir in current_directory.subdirectories.items():
            result.extend(self.search_by_size(size, sub_dir, f"{path}/{sub_dir_name}"))

        return result

    def search_by_extension(self, extension, current_directory=None, path=""):
        if current_directory is None:
            current_directory = self.root

        result = []
        for file_name in current_directory.files:
            if file_name.endswith(f".{extension}"):
                result.append(f"{path}/{file_name}")

        for sub_dir_name, sub_dir in current_directory.subdirectories.items():
            result.extend(self.search_by_extension(extension, sub_dir, f"{path}/{sub_dir_name}"))

        return result

    def search_by_autocomplete(self, prefix, current_directory=None, path=""):
        if current_directory is None:
            current_directory = self.root

        result = []
        for file_name in current_directory.files:
            if file_name.startswith(prefix):
                result.append(f"{path}/{file_name}")

        for sub_dir_name, sub_dir in current_directory.subdirectories.items():
            result.extend(self.search_by_autocomplete(prefix, sub_dir, f"{path}/{sub_dir_name}"))

        return result

    def _navigate_and_create_directories(self, path):
        parts = [p for p in path.split("/") if p]
        current = self.root

        for part in parts:
            current = current.add_directory(part)

        return current

    def _navigate_to_directory(self, path):
        parts = [p for p in path.split("/") if p]
        current = self.root

        for part in parts:
            if part not in current.subdirectories:
                raise ValueError(f"Directory '{part}' does not exist in path '{path}'.")
            current = current.subdirectories[part]

        return current

    def _navigate_to_node(self, path):
        parts = [p for p in path.split("/") if p]
        current = self.root

        for part in parts:
            if part in current.subdirectories:
                current = current.subdirectories[part]
            elif part in current.files:
                return current.files[part]
            else:
                raise ValueError(f"Path '{path}' does not exist.")

        return current


# Example usage:
fs = FileSystem()
fs.mkdir("/a/b/c")
fs.add_content_to_file("/a/b/c/d.txt", "hello world")
fs.add_content_to_file("/a/b/c/e.py", "print('hello')")
fs.add_content_to_file("/a/b/c/f.java", "public class Main {}")

print(fs.ls("/"))                         # return ["a"]
print(fs.search_by_size(20))               # return ["/a/b/c/d.txt", "/a/b/c/e.py", "/a/b/c/f.java"]
print(fs.search_by_extension("py"))      # return ["/a/b/c/e.py"]
print(fs.search_by_autocomplete("d"))    # return ["/a/b/c/d.txt"]
