import random
import time

def benutzeroptionen():
    option1 = input("Gib die erste Option ein (z. B. Ja): ")
    option2 = input("Gib die zweite Option ein (z. B. Nein): ")
    return option1, option2

def zufallsantwort(option1, option2):
    return random.choice([option1, option2])

if __name__ == "__main__":
    print("Willkommen zum elektronischen Entscheidungswürfel!")
    option1, option2 = benutzeroptionen()
    input("Drücke Enter, um eine zufällige Entscheidung zu erhalten...")

    # Zufällige Wartezeit zwischen 5 und 7 Sekunden
    wartezeit = random.uniform(5, 7)
    print(f"Denk nach", end="", flush=True)
    for i in range(int(wartezeit)):
        time.sleep(1)
        print(".", end="", flush=True)
    rest = wartezeit - int(wartezeit)
    if rest > 0:
        time.sleep(rest)

    print("\nAntwort:", zufallsantwort(option1, option2))
