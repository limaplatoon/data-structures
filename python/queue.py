class Queue:
  def __init__(self):
    self.length = 0
    self.queue = []


  def enqueue(self,data):
    self.queue.append(data)
    self.length += 1

  def dequeue(self):
    self.queue.pop(0)
    self.length -= 1

  def size(self):
    return self.length

q =  Queue()
a = 'a'
b = 'b'
c = 'c'
d = 'd'

print(q.queue)
q.enqueue(a)
q.enqueue(b)
q.enqueue(c)
q.enqueue(d)
print(q.queue, q.length)
q.dequeue()
print(q.queue, q.length)