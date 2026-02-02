import math

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division (first number / second number)")
print("5. Division (second number / first number)")
print("6. Comparison (first number > second number)")
print("7. Comparison (first number < second number)")
print("8. Comparison (first number == second number)")
print("9. Logarithm of first number (base e)")
print("10. Logarithm of second number (base e)")
print("11. Logarithm of first number (base 10)")
print("12. Logarithm of second number (base 10)")
print("13. Logarithm of second number with base first number")
print("14. Logarithm of first number with base second number")
print("15. Exponential of first number")
print("16. Exponential of second number")
print("17. Square root of first number")
print("18. Square root of second number")
print("19. Power (first number ^ second number)")
print("20. Power (second number ^ first number)")
a = int(input("Enter your choice (1-20): "))
b = float(input("Enter first number: "))
c = float(input("Enter second number: "))
if a == 1:
    print("Addition: ", b + c)
elif a == 2:
    print("Subtraction: ", b - c)
elif a == 3:
    print("Multiplication: ", b * c)
elif a == 4:
    if c != 0:
        print("Division: ", b / c)
    else:
        print("Error: Division by zero")
elif a == 5:
    if b != 0:
        print("Division: ", c / b)
    else:
        print("Error: Division by zero")
elif a == 6:
    print("Comparison (b > c): ", b > c)
elif a == 7:
    print("Comparison (b < c): ", b < c)
elif a == 8:
    print("Comparison (b == c): ", b == c)
elif a == 9:
    print("Logarithm of first number is : ", math.log(b))
elif a == 10:
    print("Logarithm of second number is : ", math.log(c))
elif a == 11:
    print("Logarithm at base 10 of first number is : ", math.log10(b))
elif a == 12:
    print("Logarithm at base 10 of second number is : ", math.log10(c))
elif a == 13:
    print("Logarithm at base first number of second number is : ", math.log(c , b))
elif a == 14:
    print("Logarithm at base second number of first number is : ", math.log(b , c))
elif a == 15:
    print("Exponential of first number is : ", math.exp(b))
elif a == 16:
    print("Exponential of second number is : ", math.exp(c))
elif a == 17:
    print("Square root of first number is : ", math.sqrt(b))
elif a == 18:
    print("Square root of second number is : ", math.sqrt(c))
elif a == 19:
    print("Power (first number ^ second number) is : ", math.pow(b, c))
elif a == 20:
    print("Power (second number ^ first number) is : ", math.pow(c, b))
else:
    print("Invalid choice")