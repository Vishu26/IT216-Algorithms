####  hash_function = keys mod 10 ####

class hash_table:

    def __init__(self):
        self.hash_function = lambda key: key%10
        self.table = [[] for i in range(10)]

    def insert(self, value):
        self.table[self.hash_function(value)].append(value)

    def search(self, value):
        ind = self.table[self.hash_function(value)].index(value)
        return ind if ind!=-1 else None

    def delete(self, value):
        ind = self.search(value)
        if ind:
            self.table[self.hash_function(value)].remove(value)
        else:
            print('The entered value does not exist')
    def __str__(self):
        return self.table

table = hash_table()
