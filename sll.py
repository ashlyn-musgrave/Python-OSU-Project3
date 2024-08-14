# Name: Ashlyn Musgrave
# OSU Email: musgraas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 3 : Linked List and ADT Implementation
# Due Date: November 6, 2023
# Description: This code defines the class 'LinkedList' that represents a singly linked list and provides
# various methods for manipulating the linked list


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list
        """
        # Create a new node with the given value
        new_node = SLNode(value)

        # Set the new node's 'next' to the current first node
        new_node.next = self._head.next

        # Update the head's 'next' to point to the new node
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list
        """

        # Create a new node with the given value
        new_node = SLNode(value)

        # Find the last node in the list
        current = self._head
        while current.next:
            current = current.next

        # Insert the new node at the end
        current.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts a new value at the specified index position in the linked list
        """
        if index < 0:
            raise SLLException("Invalid index: Index cannot be negative")

        # Create a new node with the given value
        new_node = SLNode(value)
        current = self._head
        position = 0

        # Find the position to insert the new node
        while current and position < index:
            current = current.next
            position += 1

        if position < index or not current:
            raise SLLException("Invalid index: Index is out of range")

        # Insert the new node at the specified index
        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list
        """
        if index < 0:
            raise SLLException("Invalid index: Index cannot be negative")

        current = self._head
        position = 0

        # Find the node before the node to be removed
        while current.next and position < index:
            current = current.next
            position += 1

        if position < index or not current.next:
            raise SLLException("Invalid index: Index is out of range")

        # Remove the node at the specified index
        current.next = current.next.next

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end, and removes the first node that matches the
        provided value
        """
        current = self._head

        # Find the node before the node to be removed
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            # Node with the specified value found, remove it
            current.next = current.next.next
            return True
        else:
            # Node with the specified value not found
            return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided value
        """
        count = 0
        current = self._head.next

        # Iterate through the linked list to check if the value stored in the current node is equal to the provided value
        # If it matches, increment the count variable by 1.
        while current:
            if current.value == value:
                count += 1
            current = current.next

        return count

    def find(self, value: object) -> bool:
        """
        This method returns a Boolean value based on whether the provided value exists in the list
        """
        current = self._head.next

        # Iterate through the linked list to check if the value stored in the current node is equal to the provided value
        # If there's a match, return True. If not, move to the next node in the list
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList that contains the requested number of nodes from the original
        list, starting with the node located at the requested start index
        """
        if start_index < 0 or size < 0:
            raise SLLException("Invalid start_index or size")

        current = self._head.next
        index = 0

        # Find the starting node
        while index < start_index and current:
            current = current.next
            index += 1

        if not current:
            raise SLLException("Invalid start_index")

        # Create a new instance of the "LinkedList" class that will store the elements of the slice
        new_linked_list = LinkedList()

        while size > 0 and current:
            # Add the node to the end of the new_linked_list
            new_linked_list.insert_back(current.value)
            # Move to the next node in the original list by updating the current variable
            current = current.next
            # When a new node has been added to the new_linked_list, decrement the size by 1
            size -= 1

        if size > 0:
            raise SLLException("Not enough nodes to create the requested slice")

        return new_linked_list

# ------------------------ TESTING --------------------------------------

if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
