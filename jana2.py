number=1
for row in range(1,4):
    for column in range(1,4):
        print(number,end=" ")
        number=number+1
print()


#Exception handling

try:
    length=10
    width=0
    length/width
except Exception:
    print("Division by zero is invalid!kindly change your input")

try:

    width=0
    length/width
except NameError:
    print("Division by zero is invalid!kindly change your input")
except ZeroDivisionError:
    print("Division by zero is invalid kindly change you input")

try:
    width=0
    length/width
except NameError:
    print("Division by zero is invalid!kindly change your input")
except ZeroDivisionError:
    print("Division by zero is invalid kindly change you input")
except Exception:
    print("Have caught a new error")
finally:
    print("finally block excuted")




