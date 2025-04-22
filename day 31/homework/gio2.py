# 2) მომხმარებელი აწერს რიცხვებს. მხოლოდ დადებითი რიცხვები ემატება სიაში, მანამ სანამ 0-ს არ შეიყვანს.
list = []
while True:
    num = int(input("Enter number: "))
    if num > 0:
        list.append(num)
    elif num == 0:
        break
print(list)