try:
    num1,num2 = eval(input("enter 2 numbers, seperated by a coma"))
    result = num1 / num2
    print("Result is",result)

except ZeroDivisionError:
    print("division by zero is an error!")
except SyntaxError:
    print("Comma is missing,enter numbers seperated by comma like this 1, 2")
except:
    print("wrong input")
else:
    print("no exceptions")

finally:
    print("this will execute")