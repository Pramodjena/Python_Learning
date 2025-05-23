# Addition:
sum_result = 5 + 3
print(sum_result)  # Output: 8

# Subtraction:
diff_result = 5 - 3
print(diff_result)  # Output: 2

# Multiplication:
prod_result = 5 * 3
print(prod_result)  # Output: 15

# Division:
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


# Modulo (%):
# It returns the remainder of the division.
# In Python, the sign of the result is always the same as the sign of the divisor (b).
# Formula: a % b = a - (b * (a // b)), where:
# - a is the dividend (the number to be divided),
# - b is the divisor,
# - // is the floor division operator.

# Example 1:
modulo_res = 17 % 5  # 17 - (5 * (17 // 5)) = 17 - (5 * 3) = 17 - 15 = 2
print(modulo_res)

# Example 2 (Negative):
modulo_res = -7 % 3  # -7 - (3 * (-7 // 3)) = -7 - (3 * -3) = -7 + 9 = 2
print(modulo_res)

# Example 3 (Negative divisor):
modulo_res = 7 % -3  # 7 - (-3 * (7 // -3)) = 7 - (-3 * -3) = 7 - 9 = -2
print(modulo_res)

