from queue import Queue

queue = Queue([10, 20, 30])
print(len(queue))
print(queue.is_empty())
print(20 in queue)
print(99 in queue)
