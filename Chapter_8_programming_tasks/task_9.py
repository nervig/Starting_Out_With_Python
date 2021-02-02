vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"


def count_vowels(string):
    amount_vowels = 0
    for letter in string:
        if letter.upper() in vowels:
            amount_vowels += 1
    return amount_vowels


def count_consonants(string):
    amount_consonants = 0
    for letter in string:
        if letter.upper() in consonants:
            amount_consonants += 1
    return amount_consonants


print("Vowels are " + str(count_vowels("Andrey Rusanov")))
print("Consonants are " + str(count_consonants("Andrey Rusanov")))