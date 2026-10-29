def count_vowels(s:str):
    vowels_dist = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    vowels = 0
    consonants = 0
    for c in s:
        if c in vowels_dist:
            vowels += 1
        elif c != vowels_dist:
            consonants += 1
    return vowels, consonants

if "__main__" == __name__:
    s = input("enter a string: ")
    vowels, consonants = count_vowels(s)
    print(f"vowels: {vowels}, consonants: {consonants}")

