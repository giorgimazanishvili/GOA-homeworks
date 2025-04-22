# 4) 0-დან 10-მდე რიცხვები დაამატე ორ სხვადასხვა სიაში: ერთში ლუწი, მეორეში კენტი.
list1=[]
list2=[]
for i in range (0,11):
    if i % 2 == 0:
        list1.append (i)
    else:
        list2.append (i)
print(list1)
print(list2)