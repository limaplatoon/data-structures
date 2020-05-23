class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        node = self.head
        string = ''
        index = 0
        while node:
            string += f"{index}. {node.data}\n"
            index += 1
            node = node.next
        return string

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
        node.next = None
        self.tail = node
        self.length += 1

    def remove(self, data):
        node = self.head
        prev = None
        while node:
            if node.data == data:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                if node.next is None:
                    self.tail = node.next
                del node
                self.length -= 1
                return True
            node = node.next
        return False

    def get(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node.data
            node = node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(10):
        ll.add(i)
    print(ll)
    print(ll.remove(0))
    print("Removed 0:")
    print(ll)
    ll.add(10)
    print("Added 10:")
    print(ll)
