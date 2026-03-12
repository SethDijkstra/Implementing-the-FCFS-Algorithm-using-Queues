# This file defines the blueprint (template) that all queues must follow.
# It also defines the error we raise when someone uses an empty queue.


# This is the error we use when someone tries to dequeue or peek
# on a queue that has no items in it.
class QueueIsEmptyError(Exception):
    pass


# This is the blueprint class. It lists all the methods every queue must have.
# The actual code for each method will be written in the other queue files.
class Queue:

    # Adds a new item to the back of the queue.
    def enqueue(self, new_item):
        pass

    # Removes the item at the front of the queue and returns it.
    def dequeue(self):
        pass

    # Returns the item at the front of the queue without removing it.
    def get_front(self):
        pass

    # Returns True if the queue has no items, False otherwise.
    def is_empty(self):
        pass

    # Removes all items from the queue.
    def clear(self):
        pass
