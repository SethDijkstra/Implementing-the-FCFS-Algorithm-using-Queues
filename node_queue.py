# This file builds a working queue using Node objects linked together.
# Each node holds one piece of data and a pointer to the next node.
# Think of it like a chain — each link knows what the next link is.

from queue_blueprint import Queue, QueueIsEmptyError


# A Node holds one item of data and knows what the next node is.
class Node:
    def __init__(self, data):
        # Store the data value and initialize the next node pointer to None
        self.data = data
        self.next_node = None


class NodeQueue(Queue):

    # Sets up the queue with no nodes.
    # front_node points to the first person in line.
    # back_node points to the last person in line.
    def __init__(self):
        # Initialize both front and back pointers to None for an empty queue
        self.front_node = None
        self.back_node = None

        # Track number of elements in queue (useful for debugging and stats)
        self.count = 0

    # Adds a new item to the back of the queue.
    # Creates a new node and attaches it to the end of the chain.
    def enqueue(self, new_item):
        # Create a new node containing the new item
        new_node = Node(new_item)

        # If the queue is empty, the new node becomes both front and back
        if self.is_empty():
            self.front_node = new_node
            self.back_node = new_node
        else:
            # Link the current back node to the new node
            self.back_node.next_node = new_node
            # Update the back pointer to the new node
            self.back_node = new_node

        # Increase element count
        self.count += 1

    # Removes the item at the front of the queue and returns it.
    # Raises QueueIsEmptyError if there is nothing in the queue.
    def dequeue(self):
        # Check if the queue is empty and raise an error if so
        if self.is_empty():
            raise QueueIsEmptyError("Cannot dequeue from an empty queue")

        # Save the data from the front node before removing it
        data = self.front_node.data

        # Move the front pointer to the next node in the queue
        self.front_node = self.front_node.next_node

        # If the queue is now empty, set the back pointer to None as well
        if self.front_node is None:
            self.back_node = None

        # Decrease element count
        self.count -= 1

        # Return the data that was removed
        return data

    # Returns the item at the front of the queue without removing it.
    # Raises QueueIsEmptyError if there is nothing in the queue.
    def get_front(self):
        if self.is_empty():
            raise QueueIsEmptyError("Cannot get front from an empty queue")

        return self.front_node.data

    # Returns the item at the back of the queue without removing it.
    # Useful for debugging or inspection.
    def get_back(self):
        if self.is_empty():
            raise QueueIsEmptyError("Cannot get back from an empty queue")

        return self.back_node.data

    # Returns True if the queue has no items, False otherwise.
    def is_empty(self):
        # The queue is empty when the front pointer is None
        return self.front_node is None

    # Returns the number of items currently in the queue.
    # Because we track count, this runs in constant time.
    def size(self):
        return self.count

    # Removes all items from the queue by removing both pointers.
    def clear(self):
        # Reset both front and back pointers to None to clear the queue
        self.front_node = None
        self.back_node = None
        self.count = 0

    # Allows iteration over the queue without modifying it.
    def __iter__(self):
        current = self.front_node
        while current is not None:
            yield current.data
            current = current.next_node

    # Returns a readable representation of the queue contents.
    # Helpful for debugging stuff
    def __str__(self):
        values = []
        current = self.front_node

        while current is not None:
            values.append(str(current.data))
            current = current.next_node

        return "Front -> " + " -> ".join(values) + " -> None"

    # Validates the internal structure of the queue.
    # Useful during debugging to ensure count matches actual nodes.
    def validate(self):
        current = self.front_node
        actual_count = 0

        while current is not None:
            actual_count += 1
            current = current.next_node

        return actual_count == self.count
