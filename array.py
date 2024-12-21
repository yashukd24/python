class DataStructure:
    def __init__(self):
        self.data = []

    # Display Data
    def display(self):
        print("Data:", self.data)

    # Append Element
    def append(self, value):
        self.data.append(value)
        print(f"Appended {value} to the data.")

    # Insert at Position
    def insert_at(self, position, value):
        if 0 <= position <= len(self.data):
            self.data.insert(position, value)
            print(f"Inserted {value} at position {position}.")
        else:
            print("Invalid position!")

    # Delete Element by Value
    def delete_by_value(self, value):
        if value in self.data:
            self.data.remove(value)
            print(f"Deleted {value}.")
        else:
            print(f"{value} not found in data.")

    # Delete Element by Position
    def delete_at(self, position):
        if 0 <= position < len(self.data):
            removed = self.data.pop(position)
            print(f"Deleted {removed} from position {position}.")
        else:
            print("Invalid position!")

    # Search for Element
    def search(self, value):
        if value in self.data:
            print(f"{value} found at position {self.data.index(value)}.")
        else:
            print(f"{value} not found.")

    # Sort Data
    def sort(self):
        self.data.sort()
        print("Data sorted.")

    # Reverse Data
    def reverse(self):
        self.data.reverse()
        print("Data reversed.")

    # Get Length of Data
    def length(self):
        print(f"Length of data: {len(self.data)}")

    # Clear Data
    def clear(self):
        self.data.clear()
        print("Data cleared.")

    # Get Element at Position
    def get_at(self, position):
        if 0 <= position < len(self.data):
            print(f"Element at position {position}: {self.data[position]}")
        else:
            print("Invalid position!")

    # Count Occurrences of a Value
    def count_occurrences(self, value):
        count = self.data.count(value)
        print(f"{value} occurs {count} times.")

    # Merge with Another List
    def merge(self, other_data):
        self.data.extend(other_data)
        print("Merged data:", self.data)

    # Slice Data
    def slice(self, start, end):
        sliced = self.data[start:end]
        print(f"Sliced data ({start}:{end}):", sliced)
        return sliced

    # Find Minimum
    def find_min(self):
        if self.data:
            print("Minimum value:", min(self.data))
        else:
            print("Data is empty!")

    # Find Maximum
    def find_max(self):
        if self.data:
            print("Maximum value:", max(self.data))
        else:
            print("Data is empty!")

    # Rotate Data
    def rotate(self, k):
        if self.data:
            k = k % len(self.data)
            self.data = self.data[-k:] + self.data[:-k]
            print(f"Data rotated by {k} positions:", self.data)
        else:
            print("Data is empty!")

    # Check if Data is Sorted
    def is_sorted(self):
        sorted_status = self.data == sorted(self.data)
        print("Data is sorted." if sorted_status else "Data is not sorted.")

# Demonstrate All Operations
if __name__ == "__main__":
    ds = DataStructure()

    # Adding elements
    ds.append(10)
    ds.append(20)
    ds.append(30)
    ds.display()

    # Insert at position
    ds.insert_at(1, 15)
    ds.display()

    # Delete by value
    ds.delete_by_value(20)
    ds.display()

    # Delete at position
    ds.delete_at(2)
    ds.display()

    # Search for a value
    ds.search(15)
    ds.search(100)

    # Sorting and reversing
    ds.append(5)
    ds.append(25)
    ds.sort()
    ds.display()
    ds.reverse()
    ds.display()

    # Length and clear
    ds.length()
    ds.clear()
    ds.display()

    # Working with more complex data
    ds.append(50)
    ds.append(40)
    ds.append(10)
    ds.append(60)
    ds.display()

    # Merge
    ds.merge([70, 80, 90])
    ds.display()

    # Minimum and Maximum
    ds.find_min()
    ds.find_max()

    # Slicing
    ds.slice(1, 4)

    # Rotation
    ds.rotate(2)
    ds.display()

    # Checking if sorted
    ds.is_sorted()
    ds.sort()
    ds.is_sorted()

    # Count occurrences
    ds.append(10)
    ds.count_occurrences(10)
