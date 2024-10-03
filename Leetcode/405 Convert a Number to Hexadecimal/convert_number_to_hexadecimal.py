import unittest


def get_hex_map():
    return {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }


def twos_complement(num):
    return num + (1 << 32)


# Time: O(1), since the largest 32 bit integer is 2^32 - 1
# Space: O(1)
def convert_to_hex(num):
    hex_map = get_hex_map()
    res = []

    if num == 0:
        return "0"

    if num < 0:
        num = twos_complement(num)

    while num > 0:
        remainder = num % 16
        res.append(hex_map[remainder])
        num = num // 16

    return "".join(res[::-1])


class TestConvertNumberToHexadecimal(unittest.TestCase):
    def test_convert_to_hex(self):
        self.assertEqual(convert_to_hex(26), "1a")
        self.assertEqual(convert_to_hex(-1), "ffffffff")


if __name__ == "__main__":
    unittest.main()
