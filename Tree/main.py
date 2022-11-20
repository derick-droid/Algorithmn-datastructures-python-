class Node:
    def __init__(self, letter):
        self.childleft = None
        self.childright = None
        self.nodedata = letter


root = Node("A")
root.childleft  =Node("B")
root.childright = Node("c")
root.childleft.childleft = Node("D")
root.childleft.childright = Node("C")
