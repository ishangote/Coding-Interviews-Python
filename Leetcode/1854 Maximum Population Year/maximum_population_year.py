import unittest


# Time: O(nlogn), where n => 2 * length of logs
# Space: O(n)
def maximum_population_year(logs):
    events = []

    for birth, death in logs:
        events.append((birth, 1))
        events.append((death, -1))

    events.sort()

    res = events[0][0]
    max_population = 1
    cur_population = 0

    for event, change in events:
        cur_population += change
        if max_population < cur_population:
            res = event
            max_population = cur_population

    return res


class TestMaximumPopulationYear(unittest.TestCase):
    def test_maximum_population_year(self):
        self.assertEqual(maximum_population_year([[1993, 1999], [2000, 2010]]), 1993)
        self.assertEqual(
            maximum_population_year([[1950, 1961], [1960, 1971], [1970, 1981]]), 1960
        )
        self.assertEqual(
            maximum_population_year(
                [
                    [2008, 2026],
                    [2004, 2008],
                    [2034, 2035],
                    [1999, 2050],
                    [2049, 2050],
                    [2011, 2035],
                    [1966, 2033],
                    [2044, 2049],
                ]
            ),
            2011,
        )


if __name__ == "__main__":
    unittest.main()
