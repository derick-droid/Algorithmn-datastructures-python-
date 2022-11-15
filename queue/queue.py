class queue:

    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def is_full(self):
        if len(self.data) < 5:
            return True
        else:
            return  False

    def enque(self, element):
        if len(self.data) == 5:
            return "overflow"
        else:
           self.data.append(element)

    def deque(self):
        if len(self.data) == 0:
            return "underflow"
        else:
            self.data.pop()


b = queue()
b.enque(2)  # put the element into the queue
b.enque(3)
b.enque(4)
b.enque(5)
print(b.data)
b.deque()  # # remove the first element that we have put in the queue
print(b.data)
