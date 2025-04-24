class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # fixed-size array
        self.head = 0  # index of front
        self.count = 0  # current number of elements
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
