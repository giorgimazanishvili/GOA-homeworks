# დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი.

num = int(input("Enter number: "))

if num > 100:
    print("თქვენ მიერ შემოტანილი რიცხვი 100ზე მეტია")
elif num < 100:
    print("თქვენ მიერ შემოტანილი რიცხვი 100ზე ნაკლებია")
else:
    print("თქვენს მიერ შემოტანილი რიცხვი 100ის ტოლია")