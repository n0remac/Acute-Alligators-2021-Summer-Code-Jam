from os import scandir, fspath
from fstree.Node import Node


'''The FileSystemTree class is the data structure which represents the folder structure used to create the dungeon.'''
class FileStructureTree:
    '''An FileSystemTree instance is created by passing the path which will be the root of the dungeon.'''
    def __init__(self, path) -> None:
        self.root = Node(None, path)    # root node which holds references to all the other nodes in the tree
        self.add_node(self.root)
    
    '''Recursively adds subfolders as nodes to the tree.'''
    def add_node(self, node):
        with scandir(node.path) as it:
            for entry in it:
                if entry.is_dir():
                    node.children.append(Node(node, entry))
                else:
                    node.files.append(entry)
        for child in node.children:
            self.add_node(child)

    '''Prints the entire folder structure using recursive calls to the node.display() method.'''
    def display(self):
        self.root.display()
