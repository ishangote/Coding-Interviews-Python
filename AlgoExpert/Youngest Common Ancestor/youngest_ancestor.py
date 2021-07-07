"""
Questions:
1. is it a BT? yes
2. ancestor of root? None
3. if only one node? return root
4. decendents always in tree? yes

Examples:
root = 
	A
  B

yca(A, B) = A

root = 
			 A
			/ \
		   B   C
		  /   / \
		 F	 E   D
		      \
			   G
			   
yca(B, F) = B
yca(A, B) = A
yca(A, D) = A
yca(A, G) = A

yca(F, E) = A
yca(B, D) = A
yca(E, D) = C

root = 
			 A
			/ \
		   B   C
		  /   / \
		 F	 E   D (2) -> height
		      \
			   G (3) -> height
			   
yca(D, G) = ?
"""
class AncestorTreeNode:
    def __init__(self, name) -> None:
        self.name = name
        self.ancestor = None

def get_height(root, decendant):
    h = 0
    while decendant != root:
        decendant = decendant.ancestor
        h += 1
    return h
    
def youngest_ancestor(root, decendant1, decendant2):
    h1, h2 = get_height(root, decendant1), get_height(root, decendant2)

    (lower_node, higher_node) = (decendant1, decendant2) if h1 > h2 else (decendant2, decendant1)

    for itr in range(abs(h1 - h2)):
        lower_node = lower_node.ancestor
    
    while lower_node != higher_node:
        lower_node, higher_node = lower_node.ancestor, higher_node.ancestor
    
    return lower_node