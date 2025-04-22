# შექმენი ფუნქცია რომელიც მოესალმება მომხმარებლის შემოტანილ სახელს მაგალითად თუ მომხმარებელმა შემოიტანა nick 
# დაპრინტეთ "hello nick!"

def greet(name):
    return "hello " + name + "!"

print(greet(input("Enter your name: ")))