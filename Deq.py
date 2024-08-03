

class DNode() :

    def __init__(self, item = None, next = None, prev = None) :
        self._item = item
        self._next = next
        self._prev = prev
        
    def getitem(self) :
        return self._item
    def getnext(self) :
        return self._next
    def getprev(self) :
        return self._prev

class Deq() :

    def __init__(self) :
        self._front = DNode()
        self._end = DNode()
        self._size = 0
        
        self._front._next = self._end
        self._end._prev = self._front
    
    def __iter__(self) :
        k = self._front._next
        while k._next :
            yield k._item 
            k = k._next

    def __str__(self) :
        if self._front._next == self._end :
            return 'Empty queue'
        s = ''
        for i in self :
            s += str(i) + '->'
        return s + 'None'

    def enqueue_front(self, item) :
        New_node = DNode(item = item, next = self._front._next, prev = self._front)  
        self._front._next._prev = New_node  
        self._front._next = New_node
        self._size += 1

    def enqueue_rear(self, item) :
        New_node = DNode(item = item, next = self._end, prev = self._end._prev)
        self._end._prev._next = New_node
        self._end._prev = New_node
        self._size += 1

    def dequeue_front(self) :
        self._front._next._next._prev = self._front
        self._front._next = self._front._next._next
        self._size -= 1

    def dequeue_rear(self) :
        self._end._prev._prev._next = self._end
        self._end._prev = self._end._prev._prev
        self._size -= 1
    def __len__(self) :
        return self._size
    
    
    def getfront(self): 
        return self._front._next
    
    
    

    
