#ფუნქციები!

#ზოგადად ფუნქცია არის ის რაც ასრულებს რაღაც მოქმედებას იმდენჯერ, რამდენჯერაც მომხმარებელი ისურვებს. 

# ფუნქციის შესაქმნელად ვიყენებთ def keyword - ს.
# def keyword - ის შემდეგ გადავცემთ ფუნქციის სახელს და ბოლოში ფრჩხილებს, რომელშიც ფუნქციას გადაეცემა არგუმენტები/პარამეტრები. 
# ფუნქცია არ იმუშავებს გამოძახების გარეშე, გამოძახებისთვის კი საკმარისია უბრალოდ დავწეროთ ფუნქციის სახელი და ფრჩხილები არგუმენტებით(თუ გვაქვს)

def secret(name):
    if name == "gio":
        return "hello " + name
    elif name == "gvanca":
        return "hello " + name
    elif name == "nika":
        return "hello " + name
    elif name == "venera":
        return "hello " + name
    elif name == "saba":
        return "hello " + name
    elif name == "irakli":
        return "hello " + name
    elif name == "xvicha":
        return "hello " + name
    elif name == "ucha":
        return "hello " + name
    elif name == "lasha":
        return "hello " + name
    elif name == "tornika":
        return "hello " + name
    else:
        return "hello world"


print(secret("gio"))
print(secret("gvanca"))
print(secret("nika"))
print(secret("venera"))
print(secret("saba"))
print(secret("irakli"))
print(secret("xvicha"))
print(secret("ucha"))
print(secret("lasha"))
print(secret("tornika"))
print(secret(""))


#ეს არის მისალმების ფუნქცია, რომელსაც გადაეცემა 1 არგუმენტი/პარამეტრი (name). გამოძახებისას ფრჩხილებში რა მნიშვნელობასაც ჩავწერთ, ის მნიშვნელობა ჩაჯდება ქვემოთ, პრინტ ფუნქციაში და გამოვა ისე, რომ ფუნქცია მოგვესალმება.