# 1.მომხმარებელი შეიყვანს რიცხვს — იკითხე მანამდე, სანამ ნულის შეყვანას არ სცდის.
num= int(input("enter namber"))
while num!=0:  
    num= int(input("enter namber"))
# 2.შეიყვანე პაროლი მანამ, სანამ სწორს (მაგ. "1234") არ ჩაწერს მომხმარებელი
password=""
while password!="1234":
    password=input("enter password")
# 3.დაბეჭდე ყველა კენტი რიცხვი 1-დან 15-მდე while ციკლით.
i=1
while i <=16:
    if i % 2 ==1:
        print(i)
    i+=1