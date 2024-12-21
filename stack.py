class Stack:
    def __init__(self, capacity=100):
        self.stack = []
        self.capacity = capacity

    # 1. Push an Element
    def push(self, value):
        if len(self.stack) < self.capacity:
            self.stack.append(value)
            print(f"Pushed {value} onto the stack.")
        else:
            print("Stack overflow! Cannot push more elements.")

    # 2. Pop an Element
    def pop(self):
        if not self.is_empty():
            value = self.stack.pop()
            print(f"Popped {value} from the stack.")
            return value
        else:
            print("Stack underflow! Cannot pop from an empty stack.")
            return None

    # 3. Peek at the Top Element
    def peek(self):
        if not self.is_empty():
            print(f"Top of the stack is: {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty!")
            return None

    # 4. Check if Stack is Empty
    def is_empty(self):
        return len(self.stack) == 0

    # 5. Check if Stack is Full
    def is_full(self):
        return len(self.stack) == self.capacity

    # 6. Get the Size of the Stack
    def size(self):
        print(f"Stack size: {len(self.stack)}")
        return len(self.stack)

    # 7. Display the Stack
    def display(self):
        if not self.is_empty():
            print("Stack (top -> bottom):", " -> ".join(map(str, self.stack[::-1])))
        else:
            print("Stack is empty!")

    # 8. Clear the Stack
    def clear(self):
        self.stack = []
        print("Stack cleared.")

    # 9. Reverse the Stack
    def reverse(self):
        self.stack = self.stack[::-1]
        print("Stack reversed.")

    # 10. Search for an Element
    def search(self, value):
        if value in self.stack:
            position = len(self.stack) - self.stack.index(value)
            print(f"Element {value} found at position (1-based): {position}")
            return position
        else:
            print(f"Element {value} not found in the stack.")
            return -1

    # 11. Sort the Stack
    def sort(self):
        self.stack.sort()
        print("Stack sorted.")

    # 12. Minimum Element in the Stack
    def find_min(self):
        if not self.is_empty():
            print(f"Minimum element in the stack: {min(self.stack)}")
            return min(self.stack)
        else:
            print("Stack is empty!")
            return None

    # 13. Maximum Element in the Stack
