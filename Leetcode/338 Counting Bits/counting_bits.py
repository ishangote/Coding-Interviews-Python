import unittest


# Time: O(log2(n))
# Space: O(1)
def number_of_1_bits(n):
    bits = 0
    while n:
        bits += n % 2
        n //= 2
    return bits


# Time: O(nlogn)
# Space: O(1)
def counting_bits_brute_force(n):
    res = []
    for i in range(0, n + 1):
        bits = number_of_1_bits(i)
        res.append(bits)

    return res


# Time: O(n)
# Space: O(n)
def counting_bits_dp(n):
    num_bits = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i

        num_bits[i] = 1 + num_bits[i - offset]

    return num_bits


class TestCountingBits(unittest.TestCase):
    def test_counting_bits_brute_force(self):
        self.assertEqual(counting_bits_brute_force(2), [0, 1, 1])
        self.assertEqual(counting_bits_brute_force(5), [0, 1, 1, 2, 1, 2])

    def test_counting_bits_dp(self):
        self.assertEqual(counting_bits_dp(2), [0, 1, 1])
        self.assertEqual(counting_bits_dp(5), [0, 1, 1, 2, 1, 2])


if __name__ == "__main__":
    unittest.main()
