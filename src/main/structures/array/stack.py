class Stack:
    def __init__(self, _max=5):
        self.__max = _max
        self.__top = -1
        self.__default = None
        self.array = [self.__default] * self.__max

    def push(self, val):
        if not self.is_full():
            self.__top += 1
            self.array[self.__top] = val
            return 0
        return -1

    def pop(self):
        if not self.is_empty():
            self.array[self.__top] = self.__default
            self.__top -= 1
            return 0
        return -1

    def is_full(self):
        return self.__top == (self.__max - 1)

    def is_empty(self):
        return self.__top == -1

    @property
    def max(self):
        return self.__max

    @property
    def top(self):
        return self.__top

    @property
    def default(self):
        return self.__default

    @max.setter
    def max(self, val=None):
        if val <= 0:
            raise ValueError('MAX must be positive')
        self.__max = val
        self.__top = -1
        self.array = [self.__default] * self.__max

    @default.setter
    def default(self, val=None):
        self.__default = val

        if self.is_empty():
            self.array = [self.__default] * self.__max
        elif self.is_full():
            return

        for i in range(self.__top + 1, self.__max):
            self.array[i] = self.__default
