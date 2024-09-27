import unittest


# Time: O(1)
# Space: O(1)
def binary_watch(turned_on):
    res = []

    for h in range(0, 12):
        for m in range(0, 60):
            current_turned_on = bin(h).count("1") + bin(m).count("1")

            if current_turned_on == turned_on:
                res.append(f"{h}:{m:02d}")

    return res


class TestBinaryWatch(unittest.TestCase):
    def test_binary_watch(self):
        self.assertEqual(
            binary_watch(1),
            [
                "0:01",
                "0:02",
                "0:04",
                "0:08",
                "0:16",
                "0:32",
                "1:00",
                "2:00",
                "4:00",
                "8:00",
            ],
        )

        self.assertEqual(binary_watch(9), [])


if __name__ == "__main__":
    unittest.main()
