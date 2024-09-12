class node:
    def __init__(self, co, ex):
        self.co = co
        self.ex = ex
        self.next = None

class poly:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, co, ex):
        newnode = node(co, ex)
        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            self.temp.next = newnode
            self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(f"{self.temp.co}^{self.temp.ex} ", end='')
            self.temp = self.temp.next
        print()

def add(poly1, poly2):
    p1 = poly1.head
    p2 = poly2.head
    obj = poly()
    while p1 != None and p2 != None:
        if p1.ex > p2.ex:
            obj.create(p1.co, p1.ex)
            p1 = p1.next
        elif p1.ex < p2.ex:
            obj.create(p2.co, p2.ex)
            p2 = p2.next
        else:
            obj.create(p1.co + p2.co, p1.ex)
            p1 = p1.next
            p2 = p2.next
    while p1 != None:
        obj.create(p1.co, p1.ex)
        p1 = p1.next
    while p2 != None:
        obj.create(p2.co, p2.ex)
        p2 = p2.next
    return obj

def Input():
    obj = poly()
    while 1:
        co = int(input("enter the coefficient:"))
        ex = int(input("enter the exponent:"))
        obj.create(co, ex)
        print("do you need to continue....yes or no")
        choice = input("enter your choice")
        if choice == 'no' or choice == 'NO':
            break
    return obj


poly1 = Input()
poly2 = Input()
poly1.display()
poly2.display()
result = add(poly1, poly2)
result.display()