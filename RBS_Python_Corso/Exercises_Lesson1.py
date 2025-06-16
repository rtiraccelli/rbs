def sum_first_n(n1, n2):
    x = 0
    for i in range(n1, n2 + 1):
        x = x + i
    return x

def exercise1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    sum = sum_first_n(a, b)
    
    print(f"The sum of numbers from {a} to {b} is: {sum}")  

if __name__ == "__main__":
    exercise1()
# This code defines a function to sum all integers between two numbers (inclusive) and prints the result.
# The function `sum_first_n` takes two integers as input and calculates the sum of all integers from the first to the second (inclusive).