# გადამეორება ფუნქციები def

# ზოგადად ფუნქცია არის ის რაც ასრულებს რაღაც მოქმედებას იმდენჯერ, რამდენჯერაც მომხმარებელი ისურვებს. 

def function():
    for i in range(10):
        print(i)

# ფუნქციის შესაქმნელად ვიყენებთ def keyword - ს.
# def keyword - ის შემდეგ გადავცემთ ფუნქციის სახელს და ბოლოში ფრჩხილებს, რომელშიც ფუნქციას გადაეცემა არგუმენტები/პარამეტრები. 
# ფუნქცია არ იმუშავებს გამოძახების გარეშე, გამოძახებისთვის კი საკმარისია უბრალოდ დავწეროთ ფუნქციის სახელი და ფრჩხილები არგუმენტებით(თუ გვაქვს)

def welcome(name):
    return "Hello, " + name + "!"
print(welcome(input("Enter your name: ")))

# ეს არის მისალმების ფუნქცია, რომელსაც გადაეცემა 1 არგუმენტი/პარამეტრი (name). გამოძახებისას ფრჩხილებში რა მნიშვნელობასაც ჩავწერთ, ის მნიშვნელობა ჩაჯდება ქვემოთ, პრინტ ფუნქციაში და გამოვა ისე, რომ ფუნქცია მოგვესალმება.


def calculator(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x // y
    else:
        return "unknown value"