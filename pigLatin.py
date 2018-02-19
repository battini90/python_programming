pyg = "ay"

Orginial_word = input("Enter a word")

if len(Orginial_word)>0 and Orginial_word.isalpha():
    print("You Entered as:", Orginial_word)
    word = Orginial_word.lower()
    first_char = word[0]
    new_word = word + first_char + pyg
    print(new_word[1:])
else:
    print("Empty string, please Enter a valid word")

