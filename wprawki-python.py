# Wprawki Python - odwracanie kolejności wprowadzonych znaków

ciag_znakow = input("Wprowadź ciąg znaków: ")

i = 1

while i <= len(ciag_znakow):
    print(ciag_znakow[-i], end = "")
    i += 1

# Wprawki Python - licznik słów w tekście

tekst = input("Wprowadź tekst, w którym chcesz policzyć słowa: ")

spacja = 0

# W pętli zliczane są spacje w tekście
for znak in tekst:
    if znak == " ":
        spacja += 1

# Słów w tekście jest o 1 więcej niż spacji
print("Liczba słów w tekscie: ", spacja + 1)

# Wprawki Python - zgadnij numer

secret_number = 555

print("""Witaj w grze!
Zgadnij mój sekretny numer.
Wprowadź liczbę całkowitą.
Powodzenia!""")

user_number = int(input("Zgadnij numer: "))

while secret_number != user_number:
    print("Ha! ha! Utknąłeś w mojej pętli!")
    user_number = int(input("Zgadnij numer: "))
    
print("Dobra robota! Jesteś wolny!")
