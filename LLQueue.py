
"""
Queue implementation using LinkedList, instead of list.
"""

from LinkedList import Node, LinkedList

class LLQueue(object):
    def __init__(self, size=0):
        self._list = LinkedList()
        self._size = size

    def enqueue(self, data):
        if (self._size > 0 and self._list.count < self._size):
            self._list.add(data)
        else:
            raise Exception("Too many items in the queue")

    def dequeue(self):
        if (self._list.count == 0):
            raise Exception("No items in the queue")
        node = self._list[0]
        del self._list[0]
        return node

    def isEmpty(self):
        return (self._list.count == 0)

    def clear(self):
        self._list.clear()

    @property
    def size(self):
        return self._size

    def __len__(self):
        return len(self._list)


if __name__ == '__main__':
    import unittest

    class LLQueueTests(unittest.TestCase):
        def setUp(self):
            self._queue = LLQueue(10)

        def test_size(self):
            print("Testing size property")
            self.assertTrue(self._queue.size, 10)

        def test_isEmpty(self):
            print("Testing isEmpty")
            self.assertTrue(self._queue.isEmpty, True)
            self._queue.enqueue(1)
            self.assertTrue(self._queue.isEmpty, False)

        def test_error_dequeue_empty_queue(self):
            print("Testing exception on dequeue() from empty Queue")
            with self.assertRaises(Exception) as context:
                self._queue.dequeue()
                self.assertTrue("No items in the queue" in context.exception)

        def test_size_raises_exception(self):
            print("Testing exception on enqueue() beyond queue size")
            for i in range(10):
                self._queue.enqueue(i)
            with self.assertRaises(Exception) as context:
                self._queue.enqueue(11)
                self.assertTrue("Too many items in the queue" in context.exception)

        def test_len(self):
            print("Test enqueue / dequeue changes length")
            for i in range(10):
                self._queue.enqueue(i)
            self.assertEqual(len(self._queue), 10)
            for i in range(4):
                self._queue.dequeue()
            self.assertEqual(len(self._queue), 6)

    # Setup testSuite and run the tests
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(LLQueueTests)
    unittest.TextTestRunner().run(suite)
