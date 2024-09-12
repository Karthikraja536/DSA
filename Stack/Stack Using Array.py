class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.top += 1
            self.arr[self.top] = data
            print(f"data {data} pushed to Stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        else:
            data = self.arr[self.top]
            self.top -= 1
            print(f"data {data} popped from Stack")


    def peek(self):
        if self.is_empty():
            print("Stack is Underflow")
            return None
        else:
            return self.arr[self.top]

    def getsize(self):
        data = self.top + 1
        return data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements from top to bottom:")
            for i in range(self.top, -1, -1):
                print(self.arr[i])



def main():
    size = int(input("Enter the size of the Stack: "))
    stack = Stack(size)

    while 1:
        print("Options: 1. Push 2. Pop 3. Peek 4. Check if Empty 5. Check if Full 6. Get Size 7. Display Stack 8. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            data = input("Enter the data to push: ")
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            top_data = stack.peek()
            if top_data is not None:
                print(f"Top data is: {top_data}")
        elif choice == 4:
            if stack.is_empty():
                print("Stack is empty!")
            else:
                print("Stack is not empty")
        elif choice == 5:
            if stack.is_full():
                print("Stack is full!")
            else:
                print("Stack is not full")
        elif choice == 6:
            print(f"Stack size: {stack.getsize()}")
        elif choice == 7:
            stack.display()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")


main()