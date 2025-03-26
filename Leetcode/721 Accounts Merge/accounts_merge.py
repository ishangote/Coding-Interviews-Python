import unittest
from collections import defaultdict


class DSNode:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


class DisjointSet:
    def __init__(self):
        self.node_map = {}

    def make_set(self, value):
        if value not in self.node_map:
            self.node_map[value] = DSNode(value)

    def union(self, value1, value2):
        node1, node2 = self.node_map[value1], self.node_map[value2]

        root1, root2 = self.find_set_node(node1), self.find_set_node(node2)

        if root1 == root2:
            return

        if root1.rank > root2.rank:
            root2.parent = root1

        elif root1.rank < root2.rank:
            root1.parent = root2

        else:
            root2.parent = root1
            root1.rank += 1

    def find_set_value(self, value):
        node = self.node_map[value]
        return self.find_set_node(node).value

    def find_set_node(self, node: DSNode):
        if node.parent != node:
            node.parent = self.find_set_node(node.parent)

        return node.parent


# Time: O(n * m), where n => number of accounts, m => max number of emails. All DS operations are O(1).
# Space: O(n * m)
def accounts_merge_union_find(accounts):
    merged_accounts = []
    email_to_name = {}
    grouped_emails = defaultdict(list)

    disjoint_set = DisjointSet()

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            disjoint_set.make_set(email)
            email_to_name[email] = name

    for account in accounts:
        first_email = account[1]
        for email in account[2:]:
            disjoint_set.union(first_email, email)

    for email in email_to_name:
        parent_email = disjoint_set.find_set_value(email)
        grouped_emails[parent_email].append(email)

    for parent_email, emails in grouped_emails.items():
        merged_accounts.append([email_to_name[parent_email]] + sorted(emails))

    return merged_accounts


# -----------------------------------Build Email Graph + DFS------------------------------------------ #


def make_graph(accounts):
    graph = defaultdict(list)
    email_to_name = {}
    for account in accounts:
        name, first_email = account[0], account[1]

        if first_email not in graph:
            graph[first_email] = []
            email_to_name[first_email] = name

        for email in account[2:]:
            email_to_name[email] = name
            graph[first_email].append(email)
            graph[email].append(first_email)

    return graph, email_to_name


def recursive_helper(email, connected_emails, visited, email_graph):
    visited.add(email)
    connected_emails.append(email)

    for connected_email in email_graph[email]:
        if connected_email not in visited:
            recursive_helper(connected_email, connected_emails, visited, email_graph)


# Time: O(n * m), where n => number of accounts, m => max number of emails
# Space:O(n * m)
def accounts_merge_dfs(accounts):
    merged_accounts = []
    email_graph, email_to_name = make_graph(accounts)
    visited = set()

    for email in email_graph:
        if email not in visited:
            connected_emails = []
            recursive_helper(email, connected_emails, visited, email_graph)
            merged_accounts.append([email_to_name[email]] + sorted(connected_emails))

    return merged_accounts


# ----------------------------------------------------------------------------- #


class TestAccountsMerge(unittest.TestCase):
    def normalize(self, accounts):
        # Normalize accounts for comparison:
        # 1. Sort the emails in each account.
        # 2. Sort the list of accounts by name and then by email list.
        normalized = []
        for account in accounts:
            name = account[0]
            emails = sorted(account[1:])
            normalized.append([name] + emails)
        normalized.sort(key=lambda x: (x[0], x[1:]))
        return normalized

    def test_single_merge(self):
        # Two accounts of "Ishan" share a common email.
        accounts = [["Ishan", "a", "b"], ["Ishan", "b", "c"]]
        expected = [["Ishan", "a", "b", "c"]]
        result = accounts_merge_dfs(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_no_merge(self):
        # Accounts for "Ishan" and "Paritosh" have no common emails.
        accounts = [["Ishan", "a"], ["Paritosh", "b"]]
        expected = [["Ishan", "a"], ["Paritosh", "b"]]
        result = accounts_merge_dfs(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_multiple_merge(self):
        # All accounts of "Ishan" merge into one because of common emails.
        accounts = [["Ishan", "a", "b"], ["Ishan", "c"], ["Ishan", "b", "d"]]
        expected = [["Ishan", "a", "b", "d"], ["Ishan", "c"]]
        result = accounts_merge_dfs(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_multiple_groups(self):
        # Two distinct groups: one for "Ishan" and one for "Paritosh".
        accounts = [
            ["Ishan", "a", "b"],
            ["Ishan", "b", "c"],
            ["Paritosh", "d"],
            ["Paritosh", "e", "d"],
        ]
        expected = [["Ishan", "a", "b", "c"], ["Paritosh", "d", "e"]]
        result = accounts_merge_dfs(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_single_account(self):
        # Single account remains unchanged.
        accounts = [["Ishan", "a", "b", "c"]]
        expected = [["Ishan", "a", "b", "c"]]
        result = accounts_merge_dfs(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))


class TestAccountsMergeUnionFind(unittest.TestCase):
    def normalize(self, accounts):
        # Normalize accounts by sorting emails in each account and then sorting the list.
        normalized = []
        for account in accounts:
            name = account[0]
            emails = sorted(account[1:])
            normalized.append([name] + emails)
        normalized.sort(key=lambda x: (x[0], x[1:]))
        return normalized

    def test_single_merge(self):
        # Two accounts of "Ishan" share a common email.
        accounts = [["Ishan", "a", "b"], ["Ishan", "b", "c"]]
        expected = [["Ishan", "a", "b", "c"]]
        result = accounts_merge_union_find(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_no_merge(self):
        # Accounts for "Ishan" and "Paritosh" have no common emails.
        accounts = [["Ishan", "a"], ["Paritosh", "b"]]
        expected = [["Ishan", "a"], ["Paritosh", "b"]]
        result = accounts_merge_union_find(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_multiple_merge(self):
        # Only merge accounts that share a common email.
        accounts = [["Ishan", "a", "b"], ["Ishan", "c"], ["Ishan", "b", "d"]]
        # "a", "b", and "d" will merge while "c" remains separate.
        expected = [["Ishan", "a", "b", "d"], ["Ishan", "c"]]
        result = accounts_merge_union_find(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_multiple_groups(self):
        # Two distinct groups: one for "Ishan" and one for "Paritosh".
        accounts = [
            ["Ishan", "a", "b"],
            ["Ishan", "b", "c"],
            ["Paritosh", "d"],
            ["Paritosh", "e", "d"],
        ]
        expected = [["Ishan", "a", "b", "c"], ["Paritosh", "d", "e"]]
        result = accounts_merge_union_find(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))

    def test_single_account(self):
        # Single account remains unchanged.
        accounts = [["Ishan", "a", "b", "c"]]
        expected = [["Ishan", "a", "b", "c"]]
        result = accounts_merge_union_find(accounts)
        self.assertEqual(self.normalize(result), self.normalize(expected))


if __name__ == "__main__":
    unittest.main()
