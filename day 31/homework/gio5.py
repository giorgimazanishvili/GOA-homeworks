# 5) დაამატე რიცხვები სიაში მანამ, სანამ მათი ჯამი არ გახდება 50-ზე მეტი
numbers = []
i = 1
total = 0
while total <= 50:
    numbers.append(i)
    total += i
    i += 1
print(numbers)