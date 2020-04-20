class queue:
    def __init__(self):
        self._data =[]
        self.size = 0
        self.front = 0
    def __len__(self):
        if self.size == 0:
            return str('queue is empty')
           
        return self.size
    def first(self):
        return self._data[self.front]
    def enqueue(self,e):
        self._data.append(e)
        self.size = self.size+1
    def dequeue(self):
        first = self._data[self.front]
        self._data[self.front] = None
        self.front = self.front+1
        self.size = self.size -1
        return first

q = queue()
q.enqueue(10)
print(len(q))
print(q._data)
q.enqueue(101)
q.dequeue()
q.dequeue()
q.enqueue(102)
q.enqueue(4345)
q.enqueue(122)
print(q._data)


