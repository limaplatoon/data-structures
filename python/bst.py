import random


class Node:
    # store your DATA and LEFT and RIGHT values here
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Value: {self.value} <- Left: {self.left} -> Right: {self.right}\n"


class Bst:
    def __init__(self):
        self.root = None

    def __repr__(self):
        string = ''
        node = self.root
        if node:
            string += str(node)
            if node.left:
                string += str(node.left)
            if node.right:
                string += str(node.right)
        return string

    def insert(self, value):
        # This is where you will insert a value into the Binary Search Tree
        node = self.root
        if node is None:
            self.root = Node(value)
            return True
        add_left = None
        while node:
            prev = node
            if value < node.value:
                node = node.left
                add_left = True
            elif value > node.value:
                node = node.right
                add_left = False
            else:
                return False
        if add_left:
            prev.left = Node(value)
        else:
            prev.right = Node(value)

    def contains(self, value):
        # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
        node = self.root
        while node:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def move(self, orphan: Node):
        node = self.root
        prev = None
        is_left = None
        while node:
            prev = node
            if orphan.value < node.value:
                node = node.left
                is_left = True
            elif orphan.value > node.value:
                node = node.right
                is_left = False
            else:
                raise Exception()
        if is_left:
            prev.left = orphan
        else:
            prev.right = orphan

    def remove(self, value):
        # this is where you will remove a value from the BST
        node = self.root
        parent = None
        while node:
            if value == node.value:
                if parent is None:
                    parent = self.root
                if node.left:
                    parent = node.left
                    if node.right:
                        self.move(node.right)
                elif node.right:
                    parent = node.right
                del node
                return True
            if value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        return False


if __name__ == '__main__':
    bst = Bst()
    numbers = []
    for i in range(100):
        number = random.randint(0, 1000)
        numbers.append(number)
        bst.insert(number)
    print(bst)
    for number in numbers:
        if not bst.contains(number):
            print(f"{number} missing")
    print("Done.")
