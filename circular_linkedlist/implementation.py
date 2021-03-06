class CircularLinkedList:
    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,e,next):
            self._element = e
            self._next = next
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def add_first(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
            newest._next = newest
        else :
            self._tail._next = newest
            newest._next=self._head
            self._head = newest
        self._size +=1
    def add_last(self,e):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size +=1

    def add_any(self,e ,pos):
        newest = self._Node(e,None)
        thead = self._head
        i = 1
        while(i<pos):
            thead = thead._next
            i+=1
        newest._next = thead._next
        thead._next = newest
        self._size +=1

    def delete_first(self):
        if self.is_empty():
            print('linked list is empty')
        else:
            value  =self._tail._next
            self._tail._next = value._next
            self._head = value._next
            self._size -=1
            if self.is_empty():
                self._tail = None
            return value._element
    
    def delete_last(self):
        if self.is_empty():
            print('linked list is empty')
        else :
            thead = self._head
            i=0
            while(i<len(self)-2):
                thead = thead._next
                i+=1
            value = thead._next
            thead._next = value._next
            self._size -=1
            return value._element
    
    def deleta_any(self,pos):
        if self.is_empty():
            print('Linked list is empty')
        else :
            thead = self._head
            i = 1
            while(i<pos):
                thead = thead._next
                i +=1
            value = thead._element
            thead._next = thead._next._next
            self._size -=1
            return value

    def display(self):
        thead = self._head
        i = 0
        while i<len(self):
            print(thead._element,end='-->')
            thead = thead._next
            i+=1
        print()


cl = CircularLinkedList()
cl.add_last(10)
cl.add_last(20)
cl.add_last(40)
cl.add_last(50)
cl.display()
cl.delete_first()
cl.display()
cl.delete_last()
cl.display()
cl.add_first(12)
cl.display()
cl.add_any(33,2)
cl.display()
cl.deleta_any(3)
cl.display()
        

            
        

