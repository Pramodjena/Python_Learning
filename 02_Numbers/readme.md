## Numbers 

### Python provides various ways to work with numbers, including integers, floats, and complex numbers.

### Basic Arithmetic Operation 

```python 

# Addition 
sum_result = 5 + 3
print(sum_result)  # Output: 8

# Subtraction
diff_result = 5 - 3
print(diff_result)  # Output: 2

# Multiplication 
prod_result = 5 * 3
print(prod_result)  # Output: 15

# Division
div_result = 5 / 3
print(div_result)  # Output: 1.6666666666666667


# Floor division:
# It divides two numbers and rounds down the result to the nearest whole number (also called the floor of the result).
# It always rounds down, even for negative numbers.

floor_div_result = 5 // 3
print(floor_div_result)  # Output: 1

floor_div_result = -5 // 3
print(floor_div_result)  # -5 / 3 = -1.666..., and floor of -1.666... is -2.

# Exponentiation:
# The ** operator is used for exponentiation. It raises the first number to the power of the second number.

# For example, 2 ** 3 means 2 to the power of 3, which
# is equal to 2 * 2 * 2 = 8.
exp_result = 2**3
print(exp_result)  # Output: 8


# Modulo:
# It returns the remainder of the division of the number before the operator by the number after the operator.
# This gives the remainder. But Python’s % always takes the sign of the divisor (b).
# For example, 17 % 5 is equal to 2, because 17 divided by
# 5 leaves a remainder of 2.
mod_result = 17 % 5
print(mod_result)  # Output: 2

```
