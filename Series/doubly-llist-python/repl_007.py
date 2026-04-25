from doubly_linked_list import DoublyLinkedList

dllist = DoublyLinkedList([1, 2, 3])
print(len(dllist))
for node in dllist:
    print(node)

for node in reversed(dllist):
    print(node)
