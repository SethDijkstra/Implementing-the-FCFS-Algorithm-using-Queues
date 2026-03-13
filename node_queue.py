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
        # Return the data that was removed
        return data

    # Returns the item at the front of the queue without removing it.
    # Raises QueueIsEmptyError if there is nothing in the queue.
    def get_front(self):
        # Check if the queue is empty and raise an error if so
        if self.is_empty():
            raise QueueIsEmptyError("Cannot get front from an empty queue")
        # Return the data from the front node without removing it
        return self.front_node.data

    # Returns True if the queue has no items, False otherwise.
    def is_empty(self):
        # The queue is empty when the front pointer is None
        return self.front_node is None

    # Removes all items from the queue by removing both pointers.
    def clear(self):
        # Reset both front and back pointers to None to clear the queue
        self.front_node = None
        self.back_node = None
