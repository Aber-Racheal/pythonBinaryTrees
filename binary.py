class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


root = None
keys = [10, 5, 15, 2, 7, 12, 20]
for key in keys:
    root = insert(root, key)


search_key = 7
result = search(root, search_key)
if result:
    print(f"Item {search_key} found in the tree.")
else:
    print(f"Item {search_key} not found in the tree.")
