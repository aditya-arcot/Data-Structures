class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        count = 0
        cur = self.root
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def insertAtStart(self, val):
        node = Node(val)
        node.next = self.root
        self.root = node

    def insertAtEnd(self, val):
        node = Node(val)
        if self.is_empty():
            self.root = node
            return

        cur = self.root
        while cur.next:
            cur = cur.next

        cur.next = node

    def search(self, val):
        cur = self.root
        while cur is not None:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def get(self, ind):
        cur = self.root
        count = 0
        while count < ind:
            if cur is None:
                return None
            cur = cur.next
            count += 1
        return cur

    def delete(self, val):
        if self.is_empty():
            return False

        if self.root.val == val:
            self.root = self.root.next
            return True

        prev = None
        cur = self.root
        while cur.val != val:
            prev = cur
            cur = cur.next
            if cur is None:
                return False
        prev.next = cur.next
        return True

    def get_nodes(self):
        cur = self.root
        nodes = []
        while cur is not None:
            nodes.append(cur.val)
            cur = cur.next
        return nodes
