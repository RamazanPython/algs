import unittest

from task_i import MyQueueSized


class TestMyQueueSized(unittest.TestCase):

    def test_1(self):
        queue = MyQueueSized(3)
        queue.push(1)
        queue.push(2)
        queue.push(3)

        assert queue.size == 3
        assert queue.queue == [1, 2, 3]
        assert queue.peek == 1

        queue.pop()
        assert queue.queue == [None, 2, 3]
        assert queue.size == 2
        assert queue.peek == 2

        queue.pop()
        assert queue.queue == [None, None, 3]
        assert queue.size == 1
        assert queue.peek == 3

    def test_2(self):
        queue = MyQueueSized(3)
        for i in range(10):
            queue.push(i)

        assert queue.queue == [0, 1, 2]
        assert queue.size == 3

    def test_3(self):
        queue = MyQueueSized(10)

        assert queue.peek is None
        assert queue.size == 0


if __name__ == '__main__':
    unittest.main()
