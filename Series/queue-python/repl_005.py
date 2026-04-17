from queue import Queue

queue = Queue([1, 2, 3])
queue.remove(2)
print(queue)
print(queue.remove(10))
