
### Tree in Python
1. A tree is heirarchiacal data structure consisting of nodes.
2. Root : One root node (Top of tree)
3. Child : node that descends from another.
4. Leaf : node with no children.
5. Edge : Connection between two nodes
5. It  is a acyclic connected graph (dont have loop)

### Why Trees Are Important in AI, ML, GenAI, and Data Science
1. AI : Decision trees, behavior trees (e.g., in game AI) 
2. ML : Algorithms like Random Forest, Gradient Boosted Trees 
3. NLP / GenAI : Syntax trees, parse trees, attention tree visualizations 
4. Data Science : Hierarchical clustering, classification paths 
5. Search Engines : Tree-based query expansion 
6. Recommendation : Hierarchical recommendation (Category trees)
7. Knowledge Representation : Ontologies and semantic trees 

```commandline
Tree Structure in Python (Simple Implementation)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)
        
root = TreeNode("Root")

child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode("Grandchild 1.1"))
child2.add_child(TreeNode("Grandchild 2.1"))
```

### Traversing Trees in Python
1. Depth-First Search (DFS)
2. Breadth-First Search (BFS) 

### Binary Tree : 
1. Binary tree is tree where each nodes has at most two children, commanly refer as left and right.

### Binary Search Tree (BST) : 
1. sorted binary tree with rules i.e left child < root < right child 
2. Enable fast searching, insertion and deletion.
```commandline
class TreeNode():
    def __init__(self, val):
       self.val=val,
       self.left=None
       self.right= None
```
### Tree Traversing Type :
1. In-Order (left -> root -> right ) - DFS : Use for sorted order in BST
2. Pre-Ordered (root -> left -> right) - DFS : Use in tree copy or serialization
3. Post-Ordered (Lef -> right -> root) - DFS: Use in delete all node, eval expression.
4. Level-Ordered Traverse - BFS (Top-Down, Level-by-Level) : 

```commandline
        1
      /   \
     2      3
    / \    / \
   4   5  6   7
  / \ /    \  /
 8  9 10   11 12
 
Preorder    [1, 2, 4, 8, 9, 5, 10, 3, 6, 11, 7, 12]
Inorder	    [8, 4, 9, 2, 10, 5, 1, 6, 11, 3, 12, 7]
Postorder   [8, 9, 4, 10, 5, 2, 11, 6, 12, 7, 3, 1]
```

```commandline
Exercise : 
📁 Root
  📁 Dcument
    📄 resume.pdf
    📄 Resport.pdf
  📁 Music
    📁 Indian Songs
      📄 Tere Liye.mp3
    📄 song.mp3
  📁 Picture
    📄 Sachinpic.png
    📄 Vacation.jpg
```

```commandline
Inordered Tree Traversinng : left => root => right
def inorder(root):
   if root:
      inorder(root.left)
      print(root.value+ " ")
      inorder(root.right)
```
[In_order Exercise](in_order_tree.py)

```commandline
Preorder : root => left => right
def pre_order(node,indent=""):
    # Print current node name
    print(indent + "File " if node.is_file else "Folder "+ node.name )
    
    # now traverse current node child and print it one by one
    for child in node.childers:
        pre_order(child,indent+" ")
```
[pre_order Exercise](pre_ordered_tree.py)

```commandline
Post-Order : left => right => root

def post_order(node, indent=""):
    # First Traverse to last file/leaf of node and print it and come back recursively.
    for child in node.childers:
        post_order(child, indent+ " ")
        print(indent + "File " if child.is_file else "Folder " + child.name)
```
[post_order exercise](post_order_tree.py)

### *PostOrdered Traversing - Deletion process* 
`Project Title: “File Cleaner Utility (Postorder Deletion Simulator)”
✅ 1. Real-World Scenario
Imagine you're building a file cleanup tool — like one used in:
A cloud storage system
Local OS disk cleanup
Deployment tools that delete temp folders
You must delete folders from the bottom-up:
You can't delete a folder until all of its contents are deleted.
That’s exactly what Postorder traversal does:
Children → Right → Parent`






