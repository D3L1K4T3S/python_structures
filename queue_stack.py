from collections import deque

"""
FIFO (First In  First Out) - queue
# Based on double-linked list - deque (double ended queue)

LIFO (Last In First Out) - stack
# Based on double-linked list or single-linked list
# All methods O(1)

Deque collections
1. O(1) - insert/delete boundary values  
2. O(n) - insert/delete
3. O(n) - get/set value

For multithreading programming, we can use LifoQueue
from queue import LifoQueue

"""


def deque_stack():
    # Create deque with max len. If maxlen = None, then deque len is infinity
    dq = deque([1, 2, 3, 4, 5], maxlen=5)

    # Add a new element right deque
    dq.append(6)
    print(dq)

    # Add a new element left deque
    dq.appendleft(0)
    print(dq)

    # Delete element right deque. Return value. Generate exception if deque empty
    el = dq.pop()
    print(el, dq, sep=" & ")

    # Delete element left deque. Return value. Generate exception if deque empty
    el = dq.popleft()
    print(el, dq, sep=" & ")

    # Expanding the queue on the right. Use any iterable object
    dq.extend([5, 6, 7, 8])
    print(dq)

    # Expanding the queue on the left. Use any iterable object
    dq.extendleft((1,))
    print(dq)

    # Insert element. If the index does not exist, that if index > 0, insert in the end, else insert in the start deque
    # If the deque have maximum elements, generate exception
    try:
        dq.insert(1, -1)
        print(dq)
    except Exception as e:
        print(e)

    # Delete element in deque. Write value, not index
    # If the value does not exist, generate exception
    dq.remove(1)
    print(dq)

    # Create copy of deque
    dq2 = dq.copy()
    print("First:", dq, "Second:", dq2, end="\n")

    # Delete all elements
    dq2.clear()
    print(dq2)

    # FIFO - queue
    fifo = deque([1, 2, 3], maxlen=3)
    print("FIFO_queue")
    # First variant
    fifo.appendleft(0)
    print(fifo)
    el = fifo.pop()
    print(el, fifo, sep=" & ")

    # Second variant
    dq.append(4)
    print(fifo)
    el = fifo.popleft()
    print(el, fifo, sep=" & ")

    # LIFO - stack
    lifo = deque([7, 8, 9], maxlen=3)
    print("LIFO_stack")
    # First variant
    lifo.append(10)
    print(lifo)
    el = lifo.pop()
    print(el, lifo, sep=" & ")

    # Second variant
    lifo.appendleft(6)
    print(lifo)
    el = lifo.popleft()
    print(el, lifo, sep=" & ")


def main():
    deque_stack()


if __name__ == '__main__':
    main()
