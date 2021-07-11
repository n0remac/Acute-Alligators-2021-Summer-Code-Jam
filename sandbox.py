import os

class Node: 
    def __init__(self, parent, path) -> None:
        self.parent = parent
        self.path = path
        self.children = []
        self.files = []

def add_node(node):
    with os.scandir(node.path) as it:
        for entry in it:
            if entry.is_dir():
                node.children.append(Node(node, entry))
            else:
                node.files.append(entry)
    for child in node.children:
        add_node(child)

rootNode = Node(None, '.')

add_node(rootNode)


# demo 
currentNode = rootNode
while True:
    print(f'in {currentNode.path}\n\tchildren: {[node.path for node in currentNode.children]}\n\tfiles: {currentNode.files}\n')
    next = int(input('enter child index, -2 for parent, or -1 to exit: '))
    if next == -1:
        break
    elif next == -2:
        currentNode = currentNode.parent
    else:
        currentNode = currentNode.children[next]


   

