# გადამეორება if elif else ( თუ , ასევე თუ , სხვა შემთხვევაში)

number = int(input("Enter your number"))               # შევქმნით ცვლადი , დავარქვით number , შემდეგ input-ის 
                                                       # გამოყენებით მომხმარებელს შემოვატანინეთ ცლადი , ეს ცვლადი 
                                                       # გავაინტეჯერეთ ანუ ვაქციეთ რიცხვად და შევინახეთ 
                                                       # ჩვენს number ცვლაში


if number < 0 :                                         # თუ მომხმარებლის შემოტანილი რიცხვი ნაკლებია 0-ზე მაშინ:
  
    print(" Number is negative ( number < 0 ) ")        #       დაპრინტე (" Number is negative ( number < 0 ) ")

elif number == 0 :                                      # ასევე თუ მომხმარებლის შემოტანილი რიცხვი უდრის 0-ს მაშინ:
   
    print(" Number equals 0 ( number = 0 ) ")           #       დაპრინტე (" Number equals 0 ( number = 0 ) ")

else:                                                   # სხვა შემთხვევაში კი:
    
    print(" Number is positive ( number > 0 ) ")        #       დაპრინტე (" Number is positive ( number > 0 ) ")



# elif = else if ( ასევე თუ ) - ვიყენებთ იმიტომ რომ if ის და else-ს გამოყენება ჩვენ შეგვიძლია მხოლოდ 1ხელ , ხოლო   elif ის გამოყენება იმდენჯერ შეგვიძლია რამდენი ვარიანტის გაკეთებაც გვსურს 