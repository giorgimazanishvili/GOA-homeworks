# შექმენი 2 ცარიელი ლისტი , შემდე for loop-ის მეშვეობით დამიპრინტე 100 ის ფარგლებში 1 ლისტში ყველა ლუწუ მეორეში ყველა კენტი რიცხვი მაგ:

# list1 = [1 , 3 , 5 , 7 , 9...]
# list2 = [2 , 4 , 6 , 8 , 10...]

list1=[]
list2=[]
for i in range (1,100):
    if i % 2 == 0:
        list1.append (i)
    else:
        list2.append (i)
print(list1)
print(list2)