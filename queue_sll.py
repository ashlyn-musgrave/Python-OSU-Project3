# Name: Ashlyn Musgrave
# OSU Email: musgraas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3: Linked List and ADT Implementation
# Due Date: November 6, 2023
# Description: This code defines the class 'Queue' that represents a queue data structure using a linked list
# as its underlying data storage


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue
        """

        # Create a new node with the provided value, which will be added to the end of the queue
        new_node = SLNode(value)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            # Connect the current tail of the queue to the new_node by setting 'next' of the current tail to the new node
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        """
        This method removes and returns the value from the beginning of the queue
        """
        if self.is_empty():
            raise QueueException("Queue is empty")

        # Assign the value of the current head element to the variable 'value'
        value = self._head.value
        # Update self._head to be the next element in the queue
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return value

    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it
        """
        if self.is_empty():
            raise QueueException("Queue is empty")
        # Return the value of the front element
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
