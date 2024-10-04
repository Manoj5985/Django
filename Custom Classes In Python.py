class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    # This method makes the class iterable
    def __iter__(self):
        yield {'length': self.length}  # First return the length
        yield {'width': self.width}    # Then return the width

# Example usage:
rect = Rectangle(10, 5)

# Iterating over the Rectangle instance
for dimension in rect:
    print(dimension)
