import os
import time

#Zmienne
oc = []
licznik = 0
inp = ""
licznik2 = 0
sa = []
sp = []


#Lista słówek
tekst1 = open('slowka_angielskie')
tekst2 = open('slowka_polskie')
sa = tekst1.readlines()
sp = tekst2.readlines()

ilosc = len(sa) - 1

#Usuwanie znaków \n
while licznik != ilosc:
        a = sa[licznik]
        a = a[:a.index("\n")]
        sa[licznik] = a

        b = sp[licznik]
        b = b[:b.index("\n")]
        sp[licznik] = b
        licznik = licznik + 1
licznik = 0

#Zamykanie plików
tekst1.close()
tekst2.close()


#Tworzenie zmiennej z oceną
while licznik != ilosc + 1:
       oc.append(0)
       licznik += 1
licznik = 0

#Start programu
print("nauka angielskiego")
print("")


powt = 0
while 1 == 1:
       #Wyświetlanie słówka i oczekiwanie na odpowiedź użytkownika
       print(sp[licznik])
       inp = input("slowo[x - off]:")

       #Możliwość wyłączenia programu
       if inp.lower() == "x":
              break

       #wyświetlanie odpowiedzi
       if inp.lower() == sa[licznik]:
              print("Dobrze")
              print("")
              oc[licznik] = oc[licznik] + 1
              print("Czekaj...")
       else:
              print("")
              print("Zle :: {a}".format(a=sa[licznik]))

              print("")
              print("Czekaj...")

       #Czyszczenie konsoli po wyśw. odp. i ++ liczba powtórzeń
       time.sleep(1.5)
       os.system("cls")
       powt += 1

       #usuwanie słów jeśli użytkownik je zna
       licznik2 = 0
       while licznik2 != ilosc + 1:
              if oc[licznik2] >= 2:
                     del sp[licznik2]
                     del sa[licznik2]
                     del oc[licznik2]
                     ilosc = ilosc - 1
                     licznik2 = licznik2 - 1
                     licznik = licznik - 1
                     
              licznik2 = licznik2 + 1

       #Powiękrzanie licznika(lub zerowanie)
       if licznik >= ilosc:
              licznik = 0
       else:
              licznik = licznik + 1

       #Jeśli pętla jest prawie pusta: koniec programu
       if ilosc == 0:
              break

#info - kontrola
print(sp)
print(sa)



#usuwanie nauczonych słówek

#Otwieranie pliku
te1 = open('slowka_angielskie', 'w+')
te2 = open('slowka_polskie' 'w+')

licznik2 = 0

#Usuwanie znaków \n
while licznik2 != ilosc + 1:
       if licznik2 == ilosc:
              te1.write(sa[licznik2])
       else:
              te1.write(sa[licznik2] + "\n")
       
       licznik2 = licznik2 + 1

#Zapis listy słowek bez tych nauczonych
licznik2 = 0
while licznik2 != ilosc + 1:
       if licznik2 == ilosc:
              te2.write(sp[licznik2])
       else:
              te2.write(sp[licznik2] + "\n")
       licznik2 = licznik2 + 1

#Zamykanie pliku
te1.close()
te2.close()

#Czas na przeczytanie wyników
time.sleep(10)
