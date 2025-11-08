class Stack:
    def __init__(self, _max=5):
        self.__max = _max
        self.__top = -1
        self.array = [None] * self.__max

    @property
    def max(self):
        return self.__max

    @property
    def top(self):
        return self.__top

    @max.setter
    def max(self, val=None):
        self.__max = val
