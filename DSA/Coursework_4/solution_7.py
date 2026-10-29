allowed = input("enter allowed: ")
words = input("enter words: ").split()

allowed = set(allowed)
print("Allowed strings: ",allowed)


def is_allowed(words, allowed):
    result = 0
    for word in words:
        is_consistant = all(char in allowed for char in word )
        if is_consistant:
            result += 1
    return result


print(is_allowed(words, allowed))