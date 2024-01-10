class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        if self.is_empty():
            self.root = Node(key)
            return

        cur = self.root
        while cur:
            if key == cur.key:
                # ignore duplicate
                return
            elif key < cur.key:
                if cur.left is None:
                    cur.left = Node(key)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(key)
                    return
                cur = cur.right

    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def delete(self, key):
        if self.is_empty():
            return False

        if key == self.root.key:
            self.root = self.__delete_node(self.root)
            return True

        parent = None
        cur = self.root
        while cur:
            if key == cur.key:
                if parent.key < cur.key:
                    parent.right = self.__delete_node(cur)
                else:
                    parent.left = self.__delete_node(cur)
                return True
            if key < cur.key:
                parent = cur
                cur = cur.left
            else:
                parent = cur
                cur = cur.right
        return False

    def __delete_node(self, node):
        # no left child
        # right child replaces node
        if node.left is None:
            return node.right

        # no right child or no children
        # left child or None replaces node
        if node.right is None:
            return node.left

        # both children
        # successor replaces node
        successor_parent = node
        successor = node.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # delete successor
        if successor_parent == node:
            node.right = successor.right
        else:
            successor_parent.left = successor.right

        # replace key
        node.key = successor.key

        return node

    def find_min(self):
        if self.is_empty():
            return None

        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.key

    def find_max(self):
        if self.is_empty():
            return None

        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.key

    def inorder(self):
        return self.__inorder(self.root)

    def __inorder(self, node):
        nodes = []
        if node:
            nodes += self.__inorder(node.left)
            nodes.append(node.key)
            nodes += self.__inorder(node.right)
        return nodes

    def preorder(self):
        return self.__preorder(self.root)

    def __preorder(self, node):
        nodes = []
        if node:
            nodes.append(node.key)
            nodes += self.__preorder(node.left)
            nodes += self.__preorder(node.right)
        return nodes

    def postorder(self):
        return self.__postorder(self.root)

    def __postorder(self, node):
        nodes = []
        if node:
            nodes += self.__postorder(node.left)
            nodes += self.__postorder(node.right)
            nodes.append(node.key)
        return nodes

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if not node:
            return 0
        return 1 + max(self.__height(node.left), self.__height(node.right))
