class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(15)

root.left = Node(10)
root.right = Node(25)

root.left.left = Node(4)
root.left.right = Node(12)

root.right.left = Node(20)
root.right.right = Node(30)

root.left.left.left = Node(2)
root.left.left.right = Node(6)


def inorder(node):
    if node is None:
        return []

    return inorder(node.left) + [node.data] + inorder(node.right)


def preorder(node):
    if node is None:
        return []

    return [node.data] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []

    return postorder(node.left) + postorder(node.right) + [node.data]


def level_order(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


print("Inorder:", *inorder(root))
print("Preorder:", *preorder(root))
print("Postorder:", *postorder(root))
print("Level-order:", *level_order(root))
