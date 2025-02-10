# while True:
#     number = int(input("This is a Number Between 1 to 10: "))  
#     if 1 <= number <= 10:
#         print("Thank You")  
#         break
#     else:
#         print("Please Try Again")  

names = ["Ali", "Ahmed", "Ahmed","Sara", "Ali", "Zain"];
unique_item=set()

for name in names:
    if name in unique_item:
        print("This is a Duplicate Item",name)
        break
    unique_item.add(name)