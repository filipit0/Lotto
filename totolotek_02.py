import random

# Zamiast wypisywac tablice recznie mozna ja wygenerowac:
tablica = list(range(1,50))

# tablica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
# 17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,
# 34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]


podane = []

print("* * * * * * * * * * * *")
print("* * *  L O T T O  * * *")
print("* * * * * * * * * * * * \n")

for x in range(1,7):
    while True:
        print("Liczba ", x, " :", end =" ") #ZMIENILEM - Wystarczy jedna zmienmna (zmienna sterujaca petle) jako licznik
        while True:
            try:
                liczba = int(input("podaj liczbe z przedziału 1-49: " ))
            except:
                print("nie podałeś liczby")
            else:
                break

        if liczba < 1 or liczba > 49:
            print("Liczba poza przedziałem 1-49")  
        elif liczba in podane:
            print("Liczby nie mogą się powtarzać")
        else:
            podane.append(liczba)
            break
            
print()
print(" Twoje liczby to: ", sorted(podane), "\n" )  #Posortowalem wyniki dla czytelnosci
wylosowane = random.sample(tablica, k = 6)
print(" wylosowane liczby to: ", sorted(wylosowane), "\n")

trafione = 0
#for x in range(6):              - TUTAJ TYLO TAKA KOSMETYKA
#    if podane[x] in wylosowane:

for wartosc in podane:
    if wartosc in wylosowane:
        trafione += 1
        print(" trafiłeś: ", wartosc  )

if trafione == 3:
    print("3 trafione")
if trafione == 4:
    print("4 trafione")
if trafione == 5:
    print("5 trafionych")
if trafione == 6:
    print("6 trafionych. GRATULACJE !!! stałeś sie bogaty :) ")
else:
    print("Nie wygrałeś żadnej nagrody (trafienia 3,4,5 lub 6 liczb)")

a = input("press any key")



    
    
 


 
