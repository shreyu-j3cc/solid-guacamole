class SimpleCalculator:
    # Method to add two numbers
    def add(self, a, b):
        return a + b

    # Method to subtract two numbers
    def subtract(self, a, b):
        return a - b

# Example usage
if __name__ == "__main__":
    calc = SimpleCalculator()
    sum_result = calc.add(10, 5)
    diff_result = calc.subtract(10, 5)

    print("Addition Result:", sum_result)
    print("Subtraction Result:", diff_result)
