#Python program to demonstrate stack implementation as it grows .
#1 . List can be used as a stack . append() and pop() . O(n)
#2. collections.deque O(1) time complexity . faster append and pop operations from both ends .
#3. queue module  is a LIFO queue which is basically a stack . Data is inserted into queue using put() and get() takes data out .

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking.
# qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.


if __name__ == "__main__":
    stack =[]
    stack.append('A')
    stack.append('B')
    stack.append('C')
    stack.append('D')
    stack.append('E')
    print (stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())