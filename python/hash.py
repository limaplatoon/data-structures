import random

from linked_list import LinkedList


class HashTable:
    def __init__(self, number_of_buckets):
        self.number_of_buckets = number_of_buckets
        self.table = [LinkedList() for _ in range(self.number_of_buckets)]

    def __repr__(self):
        string = ''
        for index, bucket in enumerate(self.table):
            string += f"{index}:\n{bucket}"
            # for node in bucket:
            #     print(node)
        return string

    def hash(self, value):
        # here is where you'll turn your 'value' into a hash value that will return the index of your table to insert value
        # IMPORTANT: Think about how you'd store values into the same index
        h = 0
        for index, char in enumerate(value[:10]):
            h += index * ord(char)
        return h % self.number_of_buckets

    def set(self, value):
        # here is where you'll perform your logic to insert the value into your table
        # you'll also call your hash method here to get the index where you'll store the value
        self.table[self.hash(value)].add(value)

    def get(self, value):
        # here is where you'll retreive your value from the hash table
        # IMPORTANT: Think about how you'd retreive a value that from an index that has multiple values
        return self.table[self.hash(value)].get(value)

    def has_key(self, value):
        # here is where you'll return a True or False value if there is a value stored at a specific index in your HashTable
        return bool(self.table[hash(value)].length)


if __name__ == '__main__':
    hash_table = HashTable(19)
    words = []
    for i in range(100):
        word = ''
        for j in range(random.randint(3, 16)):
            word += chr(random.randint(65, 90))
        data = f"{i:3} {word}"
        # print(data)
        words.append(data)
        hash_table.set(data)
    print(hash_table)
    for word in words:
        hash_word = hash_table.get(word)
        if hash_word != word:
            print(f"{word} != {hash_word}")
    print("Done.")
