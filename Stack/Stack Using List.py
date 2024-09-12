class Stack:
    def _init_(self, size):
        self.stack = []
        self.size = size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def push(self, data):
        if self.is_full():
            print("Stack is full! Cannot push the item.")
        else:
            self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop the item.")
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Cannot peek.")
            return None
        else:
            return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Displaying from top to bottom:")

            print("Stack contents:", self.stack)


size = int(input("Enter the maximum size of the stack: "))
stack = Stack(size)

while 1:
    print("Operations:  1. Push 2. Pop 3. Peek 4. Display Stack 5. Exit")

    choice = int(input("Choose an operation: "))

    if choice == 1:
        item = input("Enter an item to push onto the stack: ")
        stack.push(item)
    elif choice == 2:
        popped_item = stack.pop()
        print(f"Popped item: {popped_item}")
    elif choice == 3:
        top_item = stack.peek()
        print(f"Top item: {top_item}")
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please choose a valid option.")