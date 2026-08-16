print("this is a string")
var_int = 1
var_bool = 1.1
var_float = True
var_string = "bok"
var1 = var2 = var3 = "these three are the same"
equal_var1,equal_var2,equal_var3 = "these","variables are","created in a single line"
print(f"var1: {var1},var2:  {var2},va3: {var3}")
print(f"equal_var1: {equal_var1},equal_var2: {equal_var2},equal_var3: {equal_var3}")
print(f"printed result: {var_bool} ,{var_float}, {var_int}, {var_string},")

#enter your name?
name = str(input("Enter your name?  "))
if name == "eren":
  print("python ogrenenzi!")
else:
  print(f"Hello {name}")

import time

def dots():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")

num_list = []

# Fonksiyonu döngünün dışına taşıdık
def num_asker():
    print("\nEnter the number you want to make calculations with: ")
    nums = float(input("Number: "))

    if nums == 313131:
        print("See you soon!")
        return True  # Çıkış sinyali gönderiyor
    else:
        num_list.append(nums)  # Normal parantez () kullanıldı
        print(f"Güncel Liste: {num_list}")
        return False

# 1. Düzeltme: capitalize() sonuna parantez eklendi
starter = str(input("Hi, this is a \nsimple calculator \nwould you like to try? (y/n)> ")).capitalize()

if starter == "Y":
    is_running = True
    print("Initialising calculator code")
    dots()
    print("Calc activated.")
elif starter == "N":
    print("Calc refused.")
    is_running = False
else:
    print("Unknown command re-run the app.")
    is_running = False

# Ana döngü
while is_running:
    # Fonksiyondan gelen cevaba göre döngüyü bitiriyoruz
    should_quit = num_asker()
    if should_quit:

mylist = [] #empty list initialisation
for i in range(10,1,-1):
  mylist.append(i)
mylist.append("lists can contain many data types, and even multiple ones.")
mylist.append(True)
mylist.append(True)
mylist.append(31.31)
print(mylist)
print(f"third index is: {mylist[3]}") #print the third index only

#del
del mylist[2] #delete second index
print(mylist)

#join lists
doubled_list = mylist + mylist
print(doubled_list)

mytuple = (1,2,3.999,True,"Can contain multiple data types")
print(mytuple)
#list to tuple
listtotuple =  tuple(mylist)
print(listtotuple)
print(type(listtotuple))
print(len(listtotuple))

myset = {1,2,3}
type(myset)
#does not allow duplicate values

mydict = {"name": "eren","age": 19, "IsAlive?": True}
print(mydict)
print(mydict["age"]) #when you search for a spesific index or key in any datatype, you must use square brackets.
print(mydict.get("agx")) #will print none because agx can not be found in the key list.
print(mydict.get("age")) #will print value of the key "age" which is 19.

num1, num2 = 3, 4
#addition:
print(num1 + num2)
#subtraction:
print(num1 - num2)
#division:
print(num1 / num2)
#modulus(remainder from division):
print(num1 % num2)
#multiplication:
print(num1 * num2)
#power:
print(num1 ** num2)

#makes assigning easy:
num = 10
num += 5 #adds 5, num = 10+5=15
#can be used with all arithmetic operators