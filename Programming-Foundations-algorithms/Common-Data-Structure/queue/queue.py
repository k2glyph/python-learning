# try out the python queue functions

from collections import deque

# TODO: Create a new empty queue

queue = deque()

# TODO: Enqueue Item in queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO: print items in queue

print(queue)

# TODO: Dequeue item from queue
left= queue.popleft()
print(left)
print(queue)