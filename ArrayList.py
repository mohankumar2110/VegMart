


import ctypes

class ArrayList():

    
    __slots__ = ['_size', '_capacity', '_items']


    def __init__(self, capacity=16):
        assert(capacity > 0)
        self._size = 0
        self._capacity = capacity
        self._items = self._create_array(capacity)


    def __str__(self):
        result = '['
        for index in range(self._size):
            result += f"{self._items[index]}, "
        result += ']'
        return result


    def __len__(self):

   
        return self._size


    def __getitem__(self, index: int):
   
        if (not 0 <= index < self._size):
            raise IndexError("Index is out of range!")
        return self._items[index]


    def isEmpty(self):

        return (self._size == 0)


    def begin(self):

        return 0


    def end(self):

        return self._size


    def next(self, pos: int):

        if (not 0 <= pos < self._size):
            raise IndexError("Index is out of range!")
        return (pos + 1)


    def append(self, item):

        if (self._size == self._capacity):
            self._resize(2 * self._capacity)
        self._items[self._size] = item
        self._size += 1


    def insert(self, index: int, item):

        if (not 0 <= index <= self._size):
            raise IndexError("Index is out of range!")
        # Increase the capacity if required
        if (self._size == self._capacity):
            self._resize(2 * self._capacity)
        # Shift the block of elements
        for cursor in range(self._size, index, -1):
            self._items[cursor] = self._items[cursor-1]
        self._items[index] = item
        self._size += 1


    def delete(self, index: int):

        if (not 0 <= index < self._size):
            raise IndexError("Index is out of range!")
        # Shift the block of elements
        for cursor in range(index, self._size - 1):
            self._items[cursor] = self._items[cursor+1]
        self._size -= 1
        # It is important to remove the reference
        # to help garbage collection
        self._items[self._size] = None
        # Downsize the array if the list size is
        # falling below 25% of the capacity
        if (self._size < (self._capacity // 4)):
            self._resize(self._capacity // 2)


    def _resize(self, capacity: int):

        temp = self._create_array(capacity)
        for index in range(self._size):
            temp[index] = self._items[index]
        self._items = temp
        self._capacity = capacity


    def _create_array(self, capacity: int):

        return (ctypes.py_object * capacity)()
    
    def index(self, item) :
        for i in range(self._size) :
            if self._items[i] == item :
                return i
            

