# name='Abishek'
# for i in name:
#     print(i)
#     if(i=="b"):
#         print("This is something special!") 
 
# for color in colors:
#   print(color)
#   for i in color:
#     print (i) 
# for k in range(1,20001):
#   print(k-1)
# colors=["Red","Green","Blue","Yellow"] 
# for color in  colors:
#     print("color")
# marks=[72,45,88,30,67]
# for i in marks:
#     print(i)
#     if i >=50:
#         print(i,"pass")
#     else: 
#         print(i,"fail")
# for i in range(3,31,3):
#     print (i)
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"FizzBuzz")
    elif (i % 3 == 0):
        print(i,"Fizz")
    elif i % 5 == 0: 
        print(i,"Buzz")
    