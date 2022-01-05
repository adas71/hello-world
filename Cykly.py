from turtle import forward, penup, pendown, exitonclick, left, right
from random import randrange, uniform

for i in range(100):
    print('Nikdy nebudu odsazovat o tři mezery!')
print()

for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':  # for promenna in sekvence
    print(pozdrav + '!')
print()

n = 5
for i in range(n):
    print("hello")
print()


# for i in range(20):
#    forward(10)
#    penup()
#    forward(5)
#    pendown()

# exitonclick()

# for i in range(20):
#    forward(i)
#    penup()
#    forward(5)
#    pendown()

# exitonclick()

# for i in range(4):
#    forward(50)
#    left(90)

# exitonclick()

# for i in range(3): #dvojitý cyklus
#    for j in range(2):
#        forward(50)
#        left(90)
#        forward(50)
#        right(90)

"""
víceřídkový komentář
"""

# exitonclick()


# While cyklus
#odpoved = input('Řekni Ááá!: ')
# while odpoved != 'Ááá':
#    print('Špatně, zkus to znovu')
#    odpoved = input('Řekni Ááá! ')

# if větvení
#odpoved = input('Řekni adas71!: ')
# if odpoved == 'adas71':
#    print('Jste velmi šikovný pacient, tady máte lízátečko :)')                  #V pythonu se u větvení(if,elif..) nedává podmínka do závorky.
# print()

#while True:
    # Pokud uživatel bude pořád zadávat něco jiného pujde tenhle cyklus do nekonečna.
#    odpoved1 = input('Řekni bbb! ')
#    if odpoved1 == 'bbb':  # Příkaz break dovolí uživateli jít dál.
#        print('Bééé')
#        break
#    print('Špatně, zkus to znovu')

#print('Hotovo, ani to nebolelo.')
#print()

#for i in range(10):  # Vnější cyklus
#    for j in range(10):  # Vnitřní cyklus
#        print(j * i, end=' ')
#        if i <= j:
#           break 
#   print()

#zacatek = 0

#while soucet < 21:
#    pokracovani = input('Chceš pokračovat ? ANO/NE: ')
#    if pokracovani == 'ANO':
#        print('Hra pokračuje')
#        a = randrange(2, 9)
#        print(a)
#        zacatek = zacatek + a
#        if a >= 21:
#            print('Prohráváš!')
#        break
#    print('Hra skončila! ')
        

#soucet = 0
#while soucet < 21:
#    print('Máš', soucet, 'bodů')
#    odpoved = input('Otočit kartu? ')
#    if odpoved == 'ano':
#        karta = randrange(2, 11)
#        print('Otočil/a jsi', karta)
#        soucet = soucet + karta
#    elif odpoved == 'ne':
#        break
#    else:
#        print('Nerozumím! Odpovídej "ano", nebo "ne"')

#if soucet == 21:
#    print('Gratuluji! Vyhrál/a jsi!')
#elif soucet > 21:
#    print('Smůla!', soucet, 'bodů je moc!')
#else:
#    print('Chybělo jen', 21 - soucet, 'bodů!')

#přepisování porměnných 
oblibena_barva = 'modrá'
print(oblibena_barva)

oblibena_barva = 'žlutá'
print(oblibena_barva)



#Tenhle cyklus přiřadí všechny tyhle čísla do proměnné 
for cislo in 8, 45, 9, 21:
    print(cislo)

#Ten samý cyklus ale rozepsaný
#cislo = 8
#print(cislo)

#cislo = 45
#print(cislo)

#cislo = 9
#print(cislo)

#cislo = 21
#print(cislo)

celkem = 0

for delka_trasy in 8, 45, 9, 21:
    print('Jdu', delka_trasy, 'km do další vesnice.')
    celkem = celkem + delka_trasy

print('Celkem jsem ušla', celkem, 'km')