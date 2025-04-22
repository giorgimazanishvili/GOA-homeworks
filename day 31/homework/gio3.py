# 3) განხილე წინასწარ მოცემული სიტყვების სია და დაამატე მხოლოდ ისინი, რომლებიც ხმოვანზე იწყება. 
words = ["apple" , "banana" , "peach" , "ananas" , "orange"]
vowel_words = []
for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)
print(vowel_words)
