from queue import Queue

queue = Queue([1, 2, 3])
for item in queue:
    print(item)

for item in reversed(queue):
    print(item)
