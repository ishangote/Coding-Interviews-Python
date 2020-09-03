"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

"""
class FSTrieNode:
    def __init__(self):
        self.children = {}
        self.file_content = ""
        
    def set_file_content(self, text):
        self.file_content = text

    def append_file_content(self, text):
        self.file_content += text
        
    def get_file_content(self):
        return self.file_content
        
class FSTrie:
    def __init__(self):
        self.root = FSTrieNode()
        
    def search_fsnode(self, path):
        if path == [""]: return self.root
        cur = self.root
        for char in path:
            if char not in cur.children: return None
            cur = cur.children[char]
        return cur
                
    def insert_fsnode(self, path):
        cur = self.root
        for char in path:
            if char not in cur.children: cur.children[char] = FSTrieNode()
            cur = cur.children[char]
        return cur

class FileSystem:
    def __init__(self):
        self.fs = FSTrie()
        
    def format_path(self, path):
        return path.split('/')[1:]
        
    def ls(self, path):
        fs_path = self.format_path(path)
        fs_node = self.fs.search_fsnode(fs_path)
        if not fs_node: return None
        if fs_node.file_content: return[fs_path[-1]]
        return sorted(list(fs_node.children.keys()))

    def mkdir(self, path):
        fs_path = self.format_path(path)
        fs_node = self.fs.insert_fsnode(fs_path)
        return None

    def addContentToFile(self, filePath, content):
        file_path = self.format_path(filePath)
        fs_node = self.fs.search_fsnode(file_path)
        if not fs_node:
            fs_node = self.fs.insert_fsnode(file_path)

        if not fs_node.file_content:
            fs_node.set_file_content(content)
        else:
            fs_node.append_file_content(content)

        return None

    def readContentFromFile(self, filePath):
        file_path = self.format_path(filePath)
        fs_node = self.fs.search_fsnode(file_path)
        if fs_node: return fs_node.get_file_content()
        return None

import unittest
class TestInMemoryFileSystem(unittest.TestCase):
    def test_format_path_function(self):
        file_system = FileSystem()
        self.assertEqual(file_system.format_path("/a/b/c"), ['a', 'b', 'c'])
        self.assertEqual(file_system.format_path("/"), [''])

    def test_file_system_1(self):
        file_system = FileSystem()
        
        # Test ls
        self.assertEqual(file_system.ls("/"), [])

        # Test mkdir
        self.assertEqual(file_system.mkdir("/a/b/c"), None)

        # Test ls
        self.assertEqual(file_system.ls("/"), ["a"])
        self.assertEqual(file_system.ls("/"), ["a"])
        self.assertEqual(file_system.ls("/a"), ["b"])
        self.assertEqual(file_system.ls("/a/b"), ["c"])
        self.assertEqual(file_system.ls("/a/b/c"), [])

        # Test addContentToFile
        self.assertEqual(file_system.addContentToFile("/a/b/c/d", "hello"), None)

        # Test ls
        self.assertEqual(file_system.ls("/a/b/c/d"), ["d"])

        # Test readContentFromFile
        self.assertEqual(file_system.readContentFromFile("/a/b/c/d"), "hello")

    def test_file_system_2(self):
        file_system = FileSystem()

        # Test mkdir
        self.assertEqual(file_system.mkdir("/zijzllb"), None)

        # Test ls
        self.assertEqual(file_system.ls("/"), ["zijzllb"])
        self.assertEqual(file_system.ls("/zijzllb"), [])

        # Test mkdir
        self.assertEqual(file_system.mkdir("/r"), None)

        # Test ls
        self.assertEqual(file_system.ls("/"), ["r", "zijzllb"])
        self.assertEqual(file_system.ls("/r"), [])

        # Test addContentToFile
        self.assertEqual(file_system.addContentToFile("/zijzllb/hfktg", "d"), None)

        # Test readContentFromFile
        self.assertEqual(file_system.readContentFromFile("/zijzllb/hfktg"), "d")

        # Test ls
        self.assertEqual(file_system.ls("/zijzllb/hfktg"), ["hfktg"])

if __name__ == "__main__": unittest.main()