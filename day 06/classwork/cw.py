# if - else

name = input("Enter your name: ")

if name == "giorgi":
    print("hello giorgi")
elif name == "taso":
    print("hello taso")
elif name == "nika":
    print("hello nika")
else:
    print("wrong name!!! ERRORRR")

#Class work
#საკლასო დავალების პირობა:
#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი  რიცხვი 10-ზე ნაკლები.

num = int(input("Enter your number: "))

if num < 10:
    print("your number < 10 ")
elif num == 10:
    print("your number = 10 ")
else:
    print("your number > 10")

#მეორე დავალება:
#შეამოწმე, არის თუ არა მომხმარებლის რიცხვი დადებითი.


num = int(input("Enter your number: "))

if num < 0:
    print("your number is negative ")
elif num == 0:
    print("your number = 0  ")
else:
    print("your number is positive ")

#Types

txt = "gio"
print(type(txt))

