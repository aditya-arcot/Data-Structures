import random
from linked_list import LinkedList
from binary_search_tree import BST
from stack import Stack
from _queue import Queue

n = 100


def random_int_list(_n):
    vals = [i for i in range(_n)]
    random.shuffle(vals)
    return vals


class TestStack:
    def test_size(self):
        stack = Stack()
        assert stack.is_empty()
        assert stack.size() == 0

        vals = random_int_list(n)
        for i in vals:
            stack.push(i)
        assert not stack.is_empty()
        assert stack.size() == n

    def test_push_peek(self):
        stack = Stack()
        assert stack.peek() is None

        vals = random_int_list(n)
        for i in vals:
            stack.push(i)
            assert stack.peek() == i

    def test_push_pop(self):
        stack = Stack()
        assert stack.pop() is None

        vals = random_int_list(n)
        for i in vals:
            stack.push(i)

        for i in range(n):
            assert stack.pop() == vals[-1 - i]
        assert stack.is_empty()


class TestQueue:
    def test_size(self):
        queue = Queue()
        assert queue.is_empty()
        assert queue.size() == 0

        vals = random_int_list(n)
        for i in vals:
            queue.enqueue(i)
        assert not queue.is_empty()
        assert queue.size() == n

    def test_enqueue_peek(self):
        queue = Queue()
        assert queue.peek() is None

        vals = random_int_list(n)
        for i in vals:
            queue.enqueue(i)
            assert queue.peek() == vals[0]

    def test_enqueue_dequeue(self):
        queue = Queue()
        assert queue.dequeue() is None

        vals = random_int_list(n)
        for i in vals:
            queue.enqueue(i)

        for i in range(n):
            assert queue.dequeue() == vals[i]
        assert queue.is_empty()


class TestLinkedList:
    def test_empty(self):
        ll = LinkedList()
        assert ll.is_empty()
        ll.insertAtStart(0)
        assert not ll.is_empty()

    def test_insert_start(self):
        ll = LinkedList()
        assert ll.size() == 0

        vals = random_int_list(n)
        for i in vals:
            ll.insertAtStart(i)
        assert ll.size() == n
        assert not ll.is_empty()
        assert ll.get_nodes() == vals[::-1]

    def test_insert_at_end(self):
        ll = LinkedList()
        assert ll.size() == 0

        vals = random_int_list(n)
        for i in vals:
            ll.insertAtEnd(i)
        assert ll.size() == n
        assert not ll.is_empty()
        assert ll.get_nodes() == vals

    def test_get_search(self):
        ll = LinkedList()
        for i in range(5):
            ll.insertAtStart(i + 10)

        for i in range(5):
            assert ll.get(i)
            assert ll.search(i + 10)

        assert not ll.get(6)
        assert not ll.search(100)

    def test_delete(self):
        ll = LinkedList()
        assert not ll.delete(0)

        for i in range(10):
            ll.insertAtStart(i)

        assert not ll.delete(20)

        for i in range(10):
            assert ll.delete(i)

        assert ll.get_nodes() == []


class TestBST:
    def test_empty(self):
        bst = BST()
        assert bst.is_empty()
        bst.insert(0)
        assert not bst.is_empty()

    def test_insert_search(self):
        vals = random_int_list(n)

        bst = BST()
        for i in vals:
            bst.insert(i)
        bst.insert(0)

        for i in vals:
            assert bst.search(i)
        assert not bst.search(n)

    def test_delete_search(self):
        vals = random_int_list(n)

        bst = BST()
        assert not bst.delete(0)
        for i in vals:
            bst.insert(i)
        assert not bst.delete(n)
        for i in vals:
            assert bst.delete(i)
        assert bst.is_empty()

    def test_min_max(self):
        vals = random_int_list(n)

        bst = BST()
        assert not bst.find_min()
        assert not bst.find_max()

        for i in vals:
            bst.insert(i)

        assert bst.find_min() == 0
        assert bst.find_max() == n - 1

    def test_inorder(self):
        vals = random_int_list(n)
        bst = BST()

        assert bst.inorder() == []
        for i in vals:
            bst.insert(i)

        assert bst.inorder() == [i for i in range(n)]

    def test_preorder(self):
        bst = BST()
        assert bst.preorder() == []
        vals = [10, 2, 1, 3, 20, 15, 30]
        for i in vals:
            bst.insert(i)
        assert bst.preorder() == vals

    def test_postorder(self):
        bst = BST()
        assert bst.postorder() == []
        bst.insert(10)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.insert(20)
        bst.insert(15)
        bst.insert(30)
        assert bst.postorder() == [1, 3, 2, 15, 30, 20, 10]

    def test_height(self):
        bst = BST()
        vals = [10, 2, 1, 3, 20, 15, 30]
        for i in vals:
            bst.insert(i)
        assert bst.height() == 3
