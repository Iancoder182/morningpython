#python program that prompts user to enter a num that checks whether numb is odd or even

num = int(input("Enter Number:"))
if num==0:
    print("num is 0")

elif num % 2 == 0:
    print(num,"is even number")
else:
    print(num,"is odd number")

