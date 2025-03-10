import math

# Take user input
try:
    user_input = float(input("Enter a number: "))
    square_root = math.sqrt(user_input)
    if user_input > 0:
        natural_log = math.log(user_input)
    else:
        natural_log = "undefined (logarithm is not defined for non-positive numbers)"
    sine_value = math.sin(user_input)

    # Display the results
    print(f"Square root of {user_input}: {square_root}")
    print(f"Natural logarithm of {user_input}: {natural_log}")
    print(f"Sine of {user_input} (in radians): {sine_value}")

except ValueError:
    print("Please enter a valid number.")