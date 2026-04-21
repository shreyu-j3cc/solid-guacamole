class SimpleCalculator:
    # Method to add two numbers
    def add(self, a, b):
        return a + b

# Example usage
if __name__ == "__main__":
    calc = SimpleCalculator()
    result = calc.add(10, 5)
    print("Addition Result:", result)
