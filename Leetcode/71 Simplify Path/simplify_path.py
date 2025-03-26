import unittest


# Time: O(n), where n => length of path
# Space: O(n)
def simplify_path(path):
    split_path = path.split("/")
    res = []

    for token in split_path:
        if not token or token == ".":
            continue

        if token == "..":
            # to avoid IndexError: pop from empty list
            if res:
                res.pop()

        else:
            res.append(token)

    return "/" + "/".join(res)


# ------------------------------------------------------------ #

# * Variation: Given `cwd` which is already simplified, and a cd command (not simplified), return location


def simplify_path_change_directory(cwd, cd):
    res = [] if cd.startswith("/") else [token for token in cwd.split("/") if token]

    for token in cd.split("/"):
        if not token or token == ".":
            continue

        if token == "..":
            if res:
                res.pop()
        else:
            res.append(token)

    return "/" + "/".join(res)


class SimplifyPath(unittest.TestCase):
    def test_simplify_path(self):
        self.assertEqual(simplify_path("/home/"), "/home")
        self.assertEqual(simplify_path("/home//foo/"), "/home/foo")
        self.assertEqual(
            simplify_path("/home/user/Documents/../Pictures"), "/home/user/Pictures"
        )
        self.assertEqual(simplify_path("/../"), "/")
        self.assertEqual(simplify_path("/.../a/../b/c/../d/./"), "/.../b/d")


class SimplifyPathChangeDirectory(unittest.TestCase):
    def test_relative_path(self):
        # Appending a relative directory.
        self.assertEqual(simplify_path_change_directory("/a/b/c", "d/e"), "/a/b/c/d/e")

    def test_parent_directory(self):
        # Navigating up one level then into a new directory.
        self.assertEqual(simplify_path_change_directory("/a/b/c", "../d"), "/a/b/d")

    def test_absolute_path(self):
        # cd command is absolute, so cwd is ignored.
        self.assertEqual(simplify_path_change_directory("/a/b/c", "/x/y"), "/x/y")

    def test_multiple_parent_traversals(self):
        # Traversing up more levels than exist, should not go above root.
        self.assertEqual(simplify_path_change_directory("/a/b", "../../.."), "/")

    def test_current_directory(self):
        # Using '.' should leave the directory unchanged.
        self.assertEqual(simplify_path_change_directory("/a", "."), "/a")

    def test_complex_relative(self):
        # Combination of current directory, extra slashes, etc.
        self.assertEqual(simplify_path_change_directory("/a/b", "c/././d"), "/a/b/c/d")

    def test_root_parent(self):
        # Trying to go up from root remains at root.
        self.assertEqual(simplify_path_change_directory("/", ".."), "/")


if __name__ == "__main__":
    unittest.main()
