class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self,data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            self.temp.next = newnode
            self.temp = newnode
    def display(self):
        count = 0
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data,end=' ')
            count += 1
            self.temp = self.temp.next
        print(count)
        print()

    def insert_at_head(self,data):

        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_at_mid(self,data,pos):

        newnode = node(data)
        self.temp = self.head
        i = 1
        while i<pos-1:
            self.temp = self.temp.next
            i = i+1
        newnode.next = self.temp.next
        self.temp.next = newnode
    def insert_at_end(self,data):
        newnode = node(data)
        self.temp = self.head
        while self.temp.next is not None:
            self.temp = self.temp.next
        self.temp.next = newnode

    def delete_at_head(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
        else:
            self.temp = self.head
            while self.temp.next.next is not None:
                self.temp = self.temp.next
            self.temp.next = None

    def delete_at_mid(self, pos):
        self.temp = self.head
        i = 1
        while i < pos-1:
            self.temp = self.temp.next
            i += 1
        self.temp.next = self.temp.next.next

obj = SLL()
while 1:
    print("1.create 2.display 3.exit 4.insert_front 5.insert_mid 6.insert_end 7.delete_head 8.delete_mid 9.delete_end")
    choice = int(input("enter the choice: "))
    if choice == 1:
        data = int(input("enter the data"))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        break
    elif choice == 4:
        data = int(input("enter the data"))
        obj.insert_at_head(data)
    elif choice == 5:
        data=int(input("enter the data"))
        pos=int(input("enter position"))
        obj.insert_at_mid(data,pos)
    elif choice == 6:
        data = int(input("enter the data"))
        obj.insert_at_end(data)
    elif choice == 7:
        obj.delete_at_head()
    elif choice == 8:
        pos = int(input("Enter position: "))
        obj.delete_at_mid(pos)
    elif choice == 9:
        obj.delete_at_end()
    else:
        print("invalid choice")