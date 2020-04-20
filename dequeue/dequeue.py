class Dequeue:
    def __init__(self):
        self._data = []
        self.front = 0
    def add_first(self,e):
        self._data.insert(self.front,e)
    def add_last(self,e):
        self._data.append(e)
    def is_empty(self):
        return len(self._data)==0
    def delete_last(self):
        if is_empty():
            return "dequeue is empty"
        value = self._data.pop()
        return value

    def delete_first(self):
        if is_empty():
            return "dequeue is empty"
        value = self._data.pop(self._front)
        return value
    def first():
        return self._data[self.front]
    def __len__():
        return len(self._data)


q = Dequeue()
q.add_last(12)
q.add_first(1)

print(q._data)
    
    