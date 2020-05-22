class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    # every time we add to queue need to increment a counter
    self.queue = []
    self.total = 0

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.append(data)
    self.total +=1
    return self.queue

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the first item
      if self.total > 0:
        value = self.queue.pop(0)
        self.total -= 1
      return value


  def size(self):
    # write your code that returns the size of the Queue
    return self.total
