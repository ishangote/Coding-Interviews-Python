import unittest
from collections import defaultdict


# Time: O(V + E), where V => number of vertices, E => number of edges
# Space: O(V + E)
def find_all_recipes(recipes, ingredients, supplies):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    res = []

    for recipe, ingredient in zip(recipes, ingredients):
        in_degree[recipe] = len(ingredient)

        for ing in ingredient:
            graph[ing].append(recipe)

    stack = supplies
    recipes = set(recipes)

    while stack:
        supply = stack.pop()

        if supply in recipes:
            res.append(supply)

        for recipe in graph[supply]:
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                stack.append(recipe)

    return res


class TestFindAllRecipes(unittest.TestCase):
    def test_find_all_recipes(self):
        self.assertListEqual(
            sorted(
                find_all_recipes(
                    ["bread", "sandwich", "burger"],
                    [
                        ["yeast", "flour"],
                        ["bread", "meat"],
                        ["sandwich", "meat", "bread"],
                    ],
                    ["yeast", "flour", "meat"],
                )
            ),
            sorted(["bread", "burger", "sandwich"]),
        )


if __name__ == "__main__":
    unittest.main()
