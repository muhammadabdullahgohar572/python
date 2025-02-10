# age=20;
# day="Wednesday"
# price=12 if age>=18 else 8
# if day=="Wednesday":
#     price -= 2
# print (f"Your Ticket Has been book and ${price}")


Number = 655
Grade = ""


if Number >=101:
    print("Please cheak your number error is Number Wrong upload")
    exit()

if Number >= 90:
    Grade = "A++"
elif Number >= 80:
    Grade = "A+"
elif Number >= 70:
    Grade = "A"
elif Number >= 60:
    Grade = "B"
elif Number >= 50:
    Grade = "C"
elif Number >= 40:
    Grade = "D"
else:
    Grade = "F"


if Grade == "F":
    print("Sorry to Saye but your Fail")
else:
    print(f" Your Are Passed And your Grade is{Grade}")
