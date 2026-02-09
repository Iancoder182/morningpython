



num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter last number: "))


if operator == '+':
    ans = num1 + num2
    print(ans)

elif operator == '-':
    ans = num1 - num2
    print(ans)

elif operator == '*':
    ans = num1 * num2
    print(ans)

elif operator == '/':

    if num2 != 0:
        ans = num1 / num2
        print(ans)
    else:
        print("Math error")

else:
    print("Invalid")