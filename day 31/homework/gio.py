# 1) შექმენი სია, რომელშიც დაემატება მხოლოდ 0-დან 20-მდე ლუწი რიცხვები.
list = []
for i in range (21):
    if i % 2 == 0:
        list.append(i)
print(list)