try:
    num1,num2 = eval(input("enter two numbers, separated by a comma:"))
    result = num1/num2
    print("result is", result)
#using multiple except block for different type of error
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("comma is missing.enter numbers separated by commas like this 1,2")
except:
    print("Wrong input")
else:
    print("no exceptions")
finally:
    print("this will excecute no matter what")