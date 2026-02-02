import os
import sys

# Importujemy klasy z Twoich plików
from obiekty import Talia, Reka, Krupier
from bonusy import ManagerBonusow, LISTA_BONUSOW
from wyzejnizej import nizsza_wyzsza

def wyczysc_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("♠♥♣♦ WITAJ W BLACKJACK SUPREME ♦♣♥♠")
    
    manager_bonusow = ManagerBonusow()
    saldo = 1000  # Początkowe pieniądze gracza
    
    while saldo > 0:
        print(f"\n{'='*40}")
        print(f"💰 Twoje saldo: {saldo} PLN")
        
        # 1. ZAKŁAD GŁÓWNY
        try:
            stawka = int(input("Ile chcesz postawić? (0 aby wyjść): "))
        except ValueError:
            print("Podaj poprawną liczbę!")
            continue

        if stawka == 0:
            print("Dzięki za grę!")
            break
        if stawka > saldo:
            print("Nie masz tyle pieniędzy!")
            continue

        # 2. ZAKŁAD BONUSOWY (OPCJONALNIE)
        zaklad_bonusowy = None
        czy_bonus = input("Czy chcesz postawić zakład bonusowy? (T/N): ").strip().upper()
        if czy_bonus == 'T':
            print("\nDOSTĘPNE BONUSY:")
            for id_b, info in LISTA_BONUSOW.items():
                print(f"{id_b}: {info['nazwa']} (x{info['mnoznik']})")
            
            try:
                wybor_id = int(input("Wybierz numer bonusu: "))
                stawka_bonus = int(input("Stawka na bonus: "))
                
                if stawka_bonus <= (saldo - stawka) and wybor_id in LISTA_BONUSOW:
                    zaklad_bonusowy = {'id': wybor_id, 'stawka': stawka_bonus}
                else:
                    print("Błędny wybór lub brak środków na bonus.")
            except ValueError:
                print("Błąd danych bonusu. Pomijam bonus.")

        saldo -= stawka
        if zaklad_bonusowy:
            saldo -= zaklad_bonusowy['stawka']

        # 3. ROZDANIE KART
        talia = Talia()
        talia.tasuj()
        
        # Używamy listy rąk, aby obsłużyć ewentualny SPLIT
        rece_gracza = [Reka()]
        krupier = Krupier()

        # Rozdanie początkowe (2 karty dla gracza, 2 dla krupiera)
        rece_gracza[0].hit(talia)
        rece_gracza[0].hit(talia)
        
        krupier.hit(talia)
        krupier.hit(talia)

        print(f"\nKrupier pokazuje: [{krupier.karty[0]}] i [Karta Zakryta]")

        # 4. TURA GRACZA (obsługa wielu rąk w przypadku splitu)
        indeks_reki = 0
        while indeks_reki < len(rece_gracza):
            aktualna_reka = rece_gracza[indeks_reki]
            
            # Pętla decyzyjna dla jednej ręki
            while True:
                print(f"\n--- Ręka {indeks_reki + 1} ---")
                print(f"Twoje karty: {aktualna_reka.karty}")
                print(f"Punkty: {aktualna_reka.punkty}")

                if aktualna_reka.punkty >= 21:
                    break

                opcje = "[H]it (Dobierz) | [S]tand (Czekaj)"
                if len(aktualna_reka.karty) == 2:
                    if saldo >= stawka: opcje += " | [D]ouble (Podwój)"
                    if aktualna_reka.czy_split() and saldo >= stawka: opcje += " | [P]Split (Rozdziel)"

                decyzja = input(f"Co robisz? {opcje}: ").strip().upper()

                if decyzja == 'H':
                    aktualna_reka.hit(talia)
                    if aktualna_reka.punkty > 21:
                        print("Bust! (Przekroczyłeś 21)")
                
                elif decyzja == 'S':
                    break
                
                elif decyzja == 'D' and len(aktualna_reka.karty) == 2 and saldo >= stawka:
                    saldo -= stawka
                    # Double zwiększa stawkę dla tej konkretnej ręki (tu uproszczone, dodajemy do puli wygranej x2)
                    # Wymagałoby to struktury przechowującej stawkę per ręka, tutaj przyjmiemy, 
                    # że po prostu dobiera kartę i kończy turę, a wygrana będzie x2.
                    if aktualna_reka.double(talia):
                        print(f"Dobrano: {aktualna_reka.karty[-1]}")
                        # Oznaczamy rękę jako 'podwojoną' (można dodać atrybut do klasy Reka, 
                        # tutaj zrobimy to prosto w logice wygranej, mnożąc stawkę x2)
                        aktualna_reka.czy_podwojona = True 
                        break
                
                elif decyzja == 'P' and aktualna_reka.czy_split() and saldo >= stawka:
                    saldo -= stawka
                    nowa_reka = aktualna_reka.split()
                    rece_gracza.append(nowa_reka)
                    # Dobieramy po jednej karcie do obu rozdzielonych rąk
                    aktualna_reka.hit(talia)
                    nowa_reka.hit(talia)
                    print("Rozdzielono karty!")
                
                else:
                    print("Nieprawidłowy wybór!")
            
            indeks_reki += 1

        # 5. TURA KRUPIERA
        print(f"\n{'='*10} Tura Krupiera {'='*10}")
        print(f"Krupier odsłania: {krupier.karty}")
        krupier.graj(talia)
        print(f"Krupier kończy z kartami: {krupier.karty}")
        print(f"Punkty Krupiera: {krupier.punkty}")

        # 6. ROZLICZENIE WYNIKÓW
        laczna_wygrana = 0

        # Rozliczenie głównej gry (dla każdej ręki gracza)
        for reka in rece_gracza:
            mnoznik_reki = 2 if getattr(reka, 'czy_podwojona', False) else 1
            aktualna_stawka = stawka * mnoznik_reki
            
            if reka.punkty > 21:
                print(f"Ręka {reka.karty}: Przegrana (Bust).")
            elif krupier.punkty > 21:
                print(f"Ręka {reka.karty}: Wygrana! Krupier bust.")
                laczna_wygrana += aktualna_stawka * 2
                saldo += aktualna_stawka * 2 # Zwrot stawki + wygrana
            elif reka.punkty > krupier.punkty:
                print(f"Ręka {reka.karty}: Wygrana! ({reka.punkty} vs {krupier.punkty})")
                laczna_wygrana += aktualna_stawka * 2
                saldo += aktualna_stawka * 2
            elif reka.punkty == krupier.punkty:
                print(f"Ręka {reka.karty}: Remis.")
                laczna_wygrana += aktualna_stawka
                saldo += aktualna_stawka # Zwrot stawki
            else:
                print(f"Ręka {reka.karty}: Przegrana ({reka.punkty} vs {krupier.punkty})")

        # Rozliczenie bonusów (zawsze sprawdzamy pierwszą rękę lub sumę - wg logiki kasyna najczęściej Main Hand)
        if zaklad_bonusowy:
            wygrana_bonus = manager_bonusow.rozlicz_zaklad(zaklad_bonusowy, rece_gracza[0], krupier)
            if wygrana_bonus > 0:
                saldo += zaklad_bonusowy['stawka'] + wygrana_bonus # Zwrot + wygrana
                laczna_wygrana += wygrana_bonus

        # 7. MINI GRA: WYŻSZA / NIŻSZA (Jeśli gracz cokolwiek wygrał)
        if laczna_wygrana > 0:
            print(f"\n🎉 W tej rundzie wygrałeś łącznie: {laczna_wygrana} PLN")
            
            # Przekazujemy aktualną talię do mini-gry
            gra_wn = nizsza_wyzsza(talia)
            
            # Gracz wchodzi z kwotą, którą właśnie wygrał
            koncowa_wygrana = gra_wn.graj(laczna_wygrana)
            
            # Różnica w saldzie (gra Wyższa/Niższa operuje na kwocie wygranej, nie bezpośrednio na saldzie w trakcie gry)
            # Musimy odjąć starą wygraną (która już jest w saldzie) i dodać wynik mini gry
            saldo = saldo - laczna_wygrana + koncowa_wygrana

    print("\nKoniec gry! Zbankrutowałeś. 💸")

if __name__ == "__main__":
    main()