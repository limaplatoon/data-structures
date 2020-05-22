from python.linked_list import LinkList
from python.queue import Queue
from python.stack import Stack

linked_list = LinkList()

linked_list.add(6)
linked_list.add(9)
linked_list.add(11)
linked_list.add(4)
linked_list.add(7)

print(linked_list)

linked_list.get(9)
linked_list.remove(4)
print(linked_list)

queue = Queue()

queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.queue)
# should be 0
queue.dequeue()
print(queue.queue)

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)
stack.pop()
print(stack.stack)