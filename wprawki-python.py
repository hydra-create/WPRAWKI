# Wprawki Python - odwracanie kolejności wprowadzonych znaków

ciag_znakow = input("Wprowadź ciąg znaków: ")

i = 1

while i <= len(ciag_znakow):
    print(ciag_znakow[-i], end = "")
    i += 1
