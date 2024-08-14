# Name: Ashlyn Musgrave
# OSU Email: musgraas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3: Linked List and ADT Implementation
# Due Date: November 6, 2023
# Description: This code defines the class 'Stack' that represents a stack data structure using a linked list as its
# underlying data storage


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack.
        """

        # Create a new node with the provided value that will be added to the stack
        new_node = SLNode(value)
        # Check if the stack is empty
        if self._head is None:
            # If the stack is empty assign new_node as the head of the stack
            self._head = new_node
        else:
            # Connect the new_node to the current top of the stack
            new_node.next = self._head
            # Update self.head as the new_node, now the top element of the stack
            self._head = new_node

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value.
        """
        if self.is_empty():
            raise StackException("Cannot pop from an empty stack")

        # If the stack is not empty assign the value of the current top element to popped_value
        popped_value = self._head.value
        # Updates self._head to be the next element in the stack
        self._head = self._head.next
        return popped_value

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it
        """
        if self.is_empty():
            raise StackException("The stack is empty, there is no top element")
        # Return the top element of the stack
        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
