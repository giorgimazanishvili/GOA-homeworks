# შექმენი ცარიელი ლისტი , შემდე for loop-ის მეშვეობით დამიპრინტე 200 ის ფარგლებში ყველა მე 5ის ჯერადი რიცხვი ანუ (5 ,10 , 15 , 20 და ა.შ.)

list =[]
for i in range (1 , 200):
    if i % 5 == 0:
        list.append(i)
print(list)