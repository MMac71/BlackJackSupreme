from obiekty import Talia, Krupier, Gracz
from bonusy import ManagerBonusow
from wyzejnizej import nizsza_wyzsza
from wyświetlanie_na_ekran import wyswietl_stan_gry
from logika_gry import (
    pobierz_zaklad, 
    obsluga_bonusow, 
    tura_gracza, 
    tura_krupiera, 
    rozlicz_blackjacka, 
    obsluga_minigry
)

def gra_blackjack():
    # --- INICJALIZACJA ---
    talia = Talia()
    talia.tasuj()
    
    print("Witaj w BLACKJACK SUPREME!")
    imie = input("Podaj swoje imię: ")
    while True:
        try:
            początkowy_balans = int(input("Podaj początkowy balans (max=5000): "))
            if 0 < początkowy_balans <= 5000:
                break
            else:
                print("Balans musi być liczbą z zakresu 1-5000.")
        except ValueError:
            print("Wprowadź poprawną liczbę.")

    gracz = Gracz(imie, początkowy_balans)
    
    manager_b = ManagerBonusow()
    mini_gra = nizsza_wyzsza(talia)

    # --- PĘTLA GŁÓWNA GRY ---
    while gracz.balans > 0:
        if len(talia.karty) < 45:
            print("\n🔄 Tasowanie nowej talii...")
            talia = Talia()
            talia.tasuj()
        print(f"\n{'='*20} NOWA RUNDA {'='*20}")
        krupier = Krupier()
        gracz.reka.karty.clear()

        # 1. Pobranie zakładu i obsługa bonusów
        pobierz_zaklad(gracz)
        obsluga_bonusow(gracz)

        # 2. Rozdanie początkowe (2 karty dla każdego)
        for _ in range(2):
            gracz.reka.hit(talia)
            krupier.hit(talia)

        # 3. Tura Gracza (Zwraca listę rąk - jedną lub dwie przy splicie)
        lista_rak_gracza = tura_gracza(gracz, krupier, talia)

        # 4. Tura Krupiera (Musi widzieć wszystkie ręce gracza)
        tura_krupiera(lista_rak_gracza, krupier, talia)

        # 5. Wyświetlenie kart krupiera na koniec
        print(f"\n🃏 Krupier odsłania: {krupier.karty} (Suma: {krupier.punkty})")

        # 6. Rozliczenie Bonusów
        if gracz.aktywny_bonus:

            gracz.reka = lista_rak_gracza[0]
            wygrana_b = manager_b.rozlicz_zaklad(gracz.aktywny_bonus, gracz.reka, krupier)
            gracz.dodaj_wygrana(wygrana_b)
            gracz.aktywny_bonus = None

        # 7. Rozliczenie Blackjacka (Głównej gry)
        calkowita_wygrana = rozlicz_blackjacka(gracz, krupier, lista_rak_gracza)
        gracz.dodaj_wygrana(calkowita_wygrana)

        # 8. Obsługa Mini-gry (Wyższa/Niższa)
        laczna_stawka = gracz.biezacy_zaklad * len(lista_rak_gracza)
        zysk_netto = calkowita_wygrana - laczna_stawka
        
        obsluga_minigry(gracz, zysk_netto, mini_gra)

        # Reset ustawień po rundzie
        gracz.biezacy_zaklad = 0
        
        # Pytanie o kontynuację
        if input("\nGrasz dalej? (T/N): ").upper() != 'T':
            print(f"\nMam nadzieję, że widzimy sie niedługo znowu {gracz.imie}! Kończysz grę z wynikiem: {gracz.balans} PLN. Gratulacje!")
            break

if __name__ == "__main__":
    gra_blackjack()