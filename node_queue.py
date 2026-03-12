# This file builds a working queue using Node objects linked together.
# Each node holds one piece of data and a pointer to the next node.
# Think of it like a chain — each link knows what the next link is.
#
# TODO: Implement the Node and NodeQueue classes.
# Use a linked list approach where each node points to the next node.
# The queue should maintain front_node and back_node pointers.

from queue_blueprint import Queue, QueueIsEmptyError


# A Node holds one item of data and knows what the next node is.
class Node:
    def __init__(self, data):
        # TODO: Store the data and initialize next_node to None
        pass


class NodeQueue(Queue):

    # Sets up the queue with no nodes.
    # front_node points to the first person in line.
    # back_node points to the last person in line.
    def __init__(self):
        # TODO: Initialize front_node and back_node to None
        pass

    # Adds a new item to the back of the queue.
    # Creates a new node and attaches it to the end of the chain.
    def enqueue(self, new_item):
        # TODO: Create a new node with new_item.
        # If queue is empty, set both front_node and back_node to new_node.
        # Otherwise, attach new_node to the end and update back_node.
        pass

    # Removes the item at the front of the queue and returns it.
    # Raises QueueIsEmptyError if there is nothing in the queue.
    def dequeue(self):
        # TODO: Check if empty, raise error if so.
        # Save the data from front_node.
        # Move front_node forward.
        # If front_node is now None, also set back_node to None.
        # Return the saved data.
        pass

    # Returns the item at the front of the queue without removing it.
    # Raises QueueIsEmptyError if there is nothing in the queue.
    def get_front(self):
        # TODO: Check if empty, raise error if so.
        # Return the data from front_node.
        pass

    # Returns True if the queue has no items, False otherwise.
    def is_empty(self):
        # TODO: Return True if front_node is None, False otherwise.
        pass

    # Removes all items from the queue by removing both pointers.
    def clear(self):
        # TODO: Set both front_node and back_node to None.
        pass
