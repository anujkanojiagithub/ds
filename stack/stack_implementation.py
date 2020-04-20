class stack:
    def __init__(self):
        self._data = []
    def push(self,e):
        self._data.append(e)
    def pop(self):
        if len(self._data)==0:
            return "stack is empty"
        return self._data.pop()
    def top(self):
        if len(self._data)==0:
            return "stack is empty"
        return self._data[-1]
    def is_empty(self):
        return len(self._data)==0
