import random
def generator(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

interface = input("Möchten Sie ein Passwort generieren? (ja/nein): ")
if interface.lower() == "ja":
    try:
        length = int(input("Geben Sie die gewünschte Länge des Passworts ein (mindestens 8): "))
        password = generator(length)
        print("Generiertes Passwort:", password)
    except ValueError as e:
        print(e)

