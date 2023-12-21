class TreeNode:
    def __init__(self, id, data):
        self.data = data
        self.id = id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def print_tree(node, level=0, prefix="Root"):
    if level == 0:
        print(f"{prefix} - {node.data}")
    else:
        indent = " " * (level * 4)
        print(f"{indent}└── {node.id} - {node.data}")

    for child in node.children:
        print_tree(child, level + 1, f"{prefix}.{child.id}")


elements = [TreeNode("1", "abc")]

def createTree(root, index, i) :
    
    for j in range(i, len(elements)) :
        if (str(index) == elements[j].id) :
            root.add_child(elements[j])
             
        elif str(index) < elements[j].id and j < len(elements) - 1:
            createTree(elements[j-1] if j-1>=0 else roote, index + 1, j)
            
        else :
            return
        
roote = TreeNode("0", "Persons")
createTree(roote, 1, 0)
# Print the tree starting from the root
print_tree(roote)
