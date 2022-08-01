# Program Imię twojego ojca bez samogłosek

''' Program prezentuje to jak wygląda imie twojego ojca bez samogłosek'''

imie = input("Podaj imię twojego ojca: ")
informacja = ""
samogloski = "aąeęiuoó"

imie

for litera in imie:
    if litera.lower() not in samogloski:
        informacja += litera

print("Imię twojego ojca bez samogłosek to: ", informacja)