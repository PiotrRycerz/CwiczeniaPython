wzrost=float(input("Ile masz wzrostu? "))
waga=float(input("Jaka jest twoja waga? "))
wiek=float(input("Twój wiek to? "))
print("TABELA WSPÓŁCZYNNIKA trybu życia")
print("Praca siedząca, brak dodatkowej aktywności fizycznej\t1.2")
print("Praca niefizyczna, mało aktywny tryb życia\t1.4")
print("Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu\t1.6")
print("Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu\t1.8")
print("Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu\t2.0")
tz=float(input("Podaj swój współczynnki trybu życia:"))
#wersja dla meżczyzn
s=5
KCal=10*waga+6.25*wzrost-5*wiek+s
print("Twoje dzienne zapotrzebowanie kaloryczne wynosi:",KCal*tz,"kcal")