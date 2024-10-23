import unittest


# Time: O(n), where n => length of path
# Space: O(n)
def simplify_path(path):
    split_path = path.split("/")
    res = []

    for char in split_path:
        if not char or char == ".":
            continue

        if char == "..":
            # to avoid IndexError: pop from empty list
            if res:
                res.pop()

        else:
            res.append(char)

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


if __name__ == "__main__":
    unittest.main()
