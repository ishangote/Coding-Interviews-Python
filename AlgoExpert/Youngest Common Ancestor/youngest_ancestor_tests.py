import unittest
from youngest_ancestor import youngest_ancestor, AncestorTreeNode

"""
root =
                            A
                        /       \
                       B         C
                     /   \      /  \
                    D      E   F    G
                   / \
                  H   I
"""
class TestYoungestAncestorTree(unittest.TestCase):
    def setUp(self) -> None:
        self.A = AncestorTreeNode('A')
        self.B = AncestorTreeNode('B')
        self.C = AncestorTreeNode('C')
        self.D = AncestorTreeNode('D')
        self.E = AncestorTreeNode('E')
        self.F = AncestorTreeNode('F')
        self.G = AncestorTreeNode('G')
        self.H = AncestorTreeNode('H')
        self.I = AncestorTreeNode('I')

        self.H.ancestor = self.D
        self.I.ancestor = self.D
        self.D.ancestor = self.B
        self.E.ancestor = self.B
        self.B.ancestor = self.A
        self.F.ancestor = self.C
        self.G.ancestor = self.C
        self.C.ancestor = self.A

        self.root = self.A
    
    def test_generic(self):
        self.assertEqual(self.A, youngest_ancestor(self.root, self.E, self.F))
        self.assertEqual(self.C, youngest_ancestor(self.root, self.C, self.G))
        self.assertEqual(self.C, youngest_ancestor(self.root, self.F, self.G))
        self.assertEqual(self.B, youngest_ancestor(self.root, self.B, self.I))
        self.assertEqual(self.B, youngest_ancestor(self.root, self.H, self.E))

if __name__ == "__main__": unittest.main()
