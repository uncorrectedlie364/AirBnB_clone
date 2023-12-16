#!/usr/bin/python3
"""SimpleClass module"""

class SimpleClass:
    """A simple class demonstrating basic functionality"""

    def __init__(self, name):
        """Initialization method"""
        self.name = name

    def greet(self):
        """Method to greet"""
        print(f"Hello, {self.name}!")

# Example usage
if __name__ == "__main__":
    obj = SimpleClass("Alice")
    obj.greet()
