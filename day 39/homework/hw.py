#1. მოითხოვე მომხმარებლისგან დადებითი რიცხვი while ციკლის მეშვეობით (ანუ სანამ უარყოფითს შეიყვანს, კვლავ სთხოვე შეყვანა).
num= int(input("enter positive namber"))
while num< 0:
    num= int(input("enter positive namber"))

#2 იპოვე და დაბეჭდე 1-დან 10-მდე რიცხვების ნამრავლი while ციკლის გამოყენებით.
i=1
product=1
while i<=10:
    product *= i
    i+=1    
print(product)
#3 while ციკლით დაბეჭდე * ვარსკვლავები 5 ხაზზე (თითო ხაზზე 5 ცალი).
i=0
while i < 5:
    j=0
    while j < 5:
        print("*",end ="")
        j+=1
        print()
        i+=1
# 4 მომხმარებელი ჩაწერს სიტყვას — იმეორე მანამდე, სანამ არ დაწერს "სტოპ".
word=input("enter word")
while word.lower() !=  "სტოპ":
    word=input("enter word")
    