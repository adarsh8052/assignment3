def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

sample_number = int(input("Enter the number"))

result = factorial(sample_number)
#output
print(f"The factorial of {sample_number} is {result}.")