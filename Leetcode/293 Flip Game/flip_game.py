import unittest


def get_flip_char(char):
    return "+" if char == "-" else "-"


# Time: O(n), where n => length of current
# Space: O(1)
def flip_game(current):
    res = []

    for idx in range(len(current) - 1):
        if current[idx] == "-" or current[idx] != current[idx + 1]:
            continue

        flip_char = get_flip_char(current[idx])

        res.append(current[:idx] + flip_char + flip_char + current[idx + 2 :])

    return res


class TestFlipGame(unittest.TestCase):
    def test_flip_game(self):
        self.assertListEqual(flip_game("+"), [])
        self.assertListEqual(flip_game("+-+-"), [])
        self.assertListEqual(flip_game("--"), [])
        self.assertListEqual(flip_game("++++"), ["--++", "+--+", "++--"])


if __name__ == "__main__":
    unittest.main()
