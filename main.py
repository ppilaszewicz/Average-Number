'''You will design a program that will ask the user to input an x number of elements. Then the program will give an average. Hint( You will want to ask the user to provide the number of elements initially. )'''
''''
count=int(input("How many numbers?"))
print(count)
list =[]
for i in range(count):
 x = int(input("What is your number?"))
 list.append(x)

z = -1
y = 0
for i in range(count):
  z = z + 1
  y= list[z] + y

average = y/count
print("Your average is.. ",average) '''  

count = 0
x = 0
list = []
while x != 666:
  x= int(input("Insert your number or 666 to finish"))
  if x != 666:
    list.append(x)
    count = count +1
  else:
    break
print(list)


