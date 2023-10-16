base_value = int(input())
expression = list(input().split(" "))

if expression[1] == "+":
    if (int(expression[0]) + int(expression[2])) > base_value:
        print("OVERFLOW")
    else:
        print("OK")

else:
    if (int(expression[0]) * int(expression[2])) > base_value:
        print("OVERFLOW")
    else:
        print("OK")
