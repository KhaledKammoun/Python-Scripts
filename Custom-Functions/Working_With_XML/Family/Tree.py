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


elements = [TreeNode("1", "Kammoun"),TreeNode("2", "Khaled"), TreeNode("1", "Frikha")
            ,TreeNode("2", "Zainab"), TreeNode("3", "Ahmed"), TreeNode("4", "AhmedSon"),
            TreeNode("1", "Kchaou")
            , TreeNode("2", "Mouna"), TreeNode("3", "Tarak"),TreeNode("2", "Imed")]

def createTree(root) :
    queue = [root, elements[0]]
    root.add_child(elements[0])
    for i in range(1, len(elements)) :
        if elements[i - 1].id < elements[i].id :
            queue[len(queue) - 1].add_child(elements[i])
        else :
            while (elements[i].id <= queue[len(queue) - 1].id) :
                queue.pop()
            queue[len(queue) - 1].add_child(elements[i])
        queue.append(elements[i])
    return root
root = TreeNode("0", "Persons")
createTree(root)
# Print the tree starting from the root
print_tree(root)
