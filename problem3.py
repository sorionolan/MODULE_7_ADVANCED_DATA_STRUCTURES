class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key == node.key:
            return

        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False

        if key == node.key:
            return True

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)

    def _min_value(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current.key

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            if node.left is None and node.right is None:
                return None

            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            else:
                successor = self._min_value(node.right)
                node.key = successor
                node.right = self._delete(node.right, successor)

        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


if _name_ == "_main_":

    bst = BST()

    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)

    print(bst.inorder())  
    print(bst.search(35))  
    print(bst.search(99))  

    bst.delete(20) 
    bst.delete(40)  

    print(bst.inorder()) 
