def factorial(n):
    if n == 0:
       return 1
    else:
       return n * factorial(n  - 1)
num = int (input("enter a number: "))
if num< 0:
    print("Factorial is not defined for negative number.")
else:
      result = factorial(num)
      print(f"The factorial of {num} is {result}")  