#sentencia continue - El feo devorador de palabras

print("""
    +----------------------+
    | El Feo devorador de  |
    |   palabras [^~^]     |
    +----------------------+
    """)

userWord = input("Ingresa una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)