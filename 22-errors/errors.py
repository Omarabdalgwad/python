
try:
    value = int(input("enter a number"))
    print(value)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
print("success")
