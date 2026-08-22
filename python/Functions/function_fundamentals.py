#define a function that calculates the are of a rectangle:
def area():
  num1 = float(input("enter width of the rectangle: "))
  num2 = float(input("enter height of the rectangle: "))
  return num1 * num2 #returns the multiplication value as thre result of the function. RETURN STATEMENT MAKES THE VALUE GLOBAL****
print(f"your area is: {area()}")


#How does return work?
def multiplication(num1,num2):
  result =  num1 + num2
multiplication(3,2)
#How are functions executed?
#1. python created namespaces(the code and the function name) of the function in the memory.
#2. when function is called, python executes the functions code which is 3+2 = 5 and assigns the value to the variable "result".
#3. since there are no "return" commands at the end of the function, result value cannot get out of the function which makes it a local variable...
#4. so when the last print(result) code block tries to run, python cant find the variable result in the script because the variable wouldnt be seen as defined
#5. but if we directly used "return result" at the end, it evaluates the expression and sends back a raw value to the exact line where the function w

#****
#1. Without return
#The function calculates the value, stores it in a temporary variable (result) inside its own local scope, and then... deletes it from memory as soon as the function finishes running.
#Result: The outer code never sees it because it no longer exists.
#2. With return
#The function calculates the value and hands that value directly back to where the function was called.
#However, return by itself does not permanently save it to memory. It just delivers the value. ***To save it for the outer code to use it again for later***, you must catch it in a variable:

#you can create lists using functions inside
new_list = [i for i in range(10)]
print(new_list) #output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]