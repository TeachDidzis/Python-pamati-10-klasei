"""
sk1 = input("Ievadiet skaitli: ")
sk2 = input("Ievadiet skaitli: ")
sk3 = input("Ievadiet skaitli: ")
sk4 = input("Ievadiet skaitli: ")
sk5 = input("Ievadiet skaitli: ")

if sk1 > 0 or sk1 < 0 and sk2 > 0 or sk2 < 0 and sk3 > 0 or sk3 < 0 and sk4 > 0 or sk4 < 0 and sk5 > 0 or sk5 < 0:
    saraksts = [sk1, sk2, sk3, sk4, sk5]
    print(f"Ievadītie skaitļi ir {sk1} {sk2} {sk3} {sk4} {sk5}")
    lielakais = max(saraksts)
    mazakais = min(saraksts)
    print("Lielākais skaitlis ir: ", lielakais)
    print("Mazākais skaitlis ir: ", mazakais)
else:
    print("Nepareizi ievadīta kāda vērtība!")

"""

"""
skaitlis = "1" # Deklarēts mainīgais ar tekstuālu vērtību 1

vesels_skaitlis = int(skaitlis) # Pārveidots mainīgais uz skaitlisku, veselu vērtību 1

dec_skaitlis = float(skaitlis) # Pārveidots mainīgais decimālskaitļa formātā 1.0

# Izdrukā visas vērtības:

print(skaitlis)
print(vesels_skaitlis)
print(dec_skaitlis)

print(2**2)
    

sk1 = 0

if sk1 > 0:
    print("Skaitlis ir pozitīvs")
elif sk1 < 0:
    print("Skaitlis ir negativs")
else:
    print("Skaitlis ir 0")
    
"""

import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Make a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()
