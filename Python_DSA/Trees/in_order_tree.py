
## Tree shructure in python
class TreeNode():
    def __init__(self,value):
        self.value=value
        self.childrens=[] # Adding child to
    def add_node(self,node): # adding child node to parent
        self.childrens.append(node)

root= TreeNode("RootNode")
left=TreeNode("Child 1")
right=TreeNode("Child 2")
root.add_node(left)
root.add_node(right)

left.add_node(TreeNode("GrandChild 1"))
right.add_node(TreeNode("GrandChild 2"))

def inorder(node,indent=""):
    # if node is None:
    #     return
    print(indent+" " + node.value)
    for child in node.childrens:
        inorder(child,indent+"  ")

inorder(root)

