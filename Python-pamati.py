# Python programmēšanas pamati

#
"""
1. Problēma
    Izveido kalkulatora programmu, kas ļauj veikt pamata operācijas (* + - /) ar 2 skaitļiem.
2. Ievades dati
    Veseli vai decimālskaitļi
3. Izvades dati
    Veseli vai decimālskaitļi
4. Funkcionālās prasības
    1. Izveido funkciju 'kalkulators', kas saņem 3 mainīgo vērtības:
        a. Pirmais skaitlis "skaitlis1";
        b. Operators "operators";
        c. Otrais skaitlis "skaitlis2";
    2. Pārbaudīt ievadīto operatoru, pēc kura nosaka aritmētisko darbību (ja +, tad skaitļus saskaita);
    3. Ja dalītājs ir 0, tad kļūdas paziņojums "Nevar dalīt ar 0!"

5. Īstenošana
    Izveidotajā funkcijā lietotājs ievada prasītās vērtības un programma veic pārbaudi balstoties uz ievadīto operatoru;
    Ja operators ir +, tad saskaita;
    Ja operators ir *, tad reizina;
    ....
    Operatora pārbaudei izmanto if, elif, else nosacījumus;
    Kad ir pārbaudīts izvada aprēķināto rezultātu.

6. Ievades/izvades paraugs

    Ievadiet pirmo skaitli: 1
    Izvēlieties darbību (*, -, +, /): +
    Ievadiet otro skaitli: 2

    *izvade*
    Aprēķina rezultāts: 3

7. Papildus prasības
    Komentē koda daļas par struktūru darbību
    Ievēro koda rakstīšanas pamatprincipus
8. Testēšana

"""
def kalkulators():
    skaitlis1 = float(input("Ievadiet pirmo skaitli: "))
    operators = input("Izvēlieties operatoru (*,-,+,/)")
    skaitlis2 = float(input("Ievadiet otro skaitli: "))

    if operators == "*":
        rezultats = skaitlis1 * skaitlis2
    elif operators == "-":
        rezultats = skaitlis1 - skaitlis2
    elif operators == "+":
        rezultats = skaitlis1 + skaitlis2
    elif operators == "/":
        if skaitlis2 != 0:
            rezultats = skaitlis1 / skaitlis2
        else:
            rezultats = "Nevar dalīt ar 0!"
    else:
        rezultats = "Nepareizs operators"
    print(f"Rezultāts: {rezultats}")


kalkulators()
# Izveido skaitļu minēšanas spēli

