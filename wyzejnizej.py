import random
from obiekty import Karta, Talia
class nizsza_wyzsza:

    def __init__(self, talia: Talia):
        self.talia = talia
        
    def wartosc_porownawcza(self, karta: Karta):
            
            znaki_wartosci = {
                '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
            }

            return znaki_wartosci[karta.znak]

    def oblicz_mnoznik(self, karta: Karta, wybor: str):
        wartosc = self.wartosc_porownawcza(karta)

        if wybor == 'W':
            ilosc_wyyszych = (14 - wartosc)*4
            if ilosc_wyyszych <= 0:
                return 0
            prawdopodobienstwo = ilosc_wyyszych / 51
            mnoznik = round(1 / prawdopodobienstwo, 2)
            return mnoznik
        elif wybor == 'N':
            ilosc_nizszych = (wartosc - 2)*4
            if ilosc_nizszych <= 0:
                return 0
            prawdopodobienstwo = ilosc_nizszych / 51
            mnoznik = round(1 / prawdopodobienstwo, 2)
            return mnoznik
        else:
            return 0
        
    def pokaz_statystyki(self, karta):
            wartosc = self.wartosc_porownawcza(karta)
            
            karty_wyzsze = (14 - wartosc) * 4
            karty_nizsze = (wartosc - 2) * 4
            
            mnoznik_wyzsza = self.oblicz_mnoznik(karta, 'W')
            mnoznik_nizsza = self.oblicz_mnoznik(karta, 'N')
            
            print(f"\n📊 STATYSTYKI dla karty {karta}:")
            if mnoznik_wyzsza > 0:
                print(f"   ⬆️  Kart wyższych: {karty_wyzsze}/51 → Mnożnik (W): x{mnoznik_wyzsza}")
            else:
                print(f"   ⬆️  Kart wyższych: {karty_wyzsze}/51 → NIEMOŻLIWE")
            
            if mnoznik_nizsza > 0:
                print(f"   ⬇️  Kart niższych: {karty_nizsze}/51 → Mnożnik (N): x{mnoznik_nizsza}")
            else:
                print(f"   ⬇️  Kart niższych: {karty_nizsze}/51 → NIEMOŻLIWE")
        
    def graj(self, wygrana_poczatkowa):
        
        print("\n" + "=" * 60)
        print("🎰  MINI-GRA: WYŻSZA/NIŻSZA  🎰")
        print("\n" + "=" * 60)
        print(f"💰 Twoja obecna wygrana: {wygrana_poczatkowa} PLN")
        print("📈 Mnożnik zależy od prawdopodobieństwa!")

        wybor_gry = input("\nCzy chcesz zagrać w Wyższą/Niższą? (T/N): ").strip().upper()

        if wybor_gry != 'T':
                print(f"✅ Zabierasz swoją wygraną: {wygrana_poczatkowa} PLN 💵💵💵")
                return wygrana_poczatkowa
        
        aktualna_wygrana = wygrana_poczatkowa

        while True:
            pierwsza_karta = self.talia.dobierz()
            if not pierwsza_karta:
                print("⚠️  Brak kart w talii! Zabierasz obecną wygraną.")
                return aktualna_wygrana
            
            print(f"\n{'─' * 60}")
            print(f"💰 Twoja obecna wygrana: {round(aktualna_wygrana, 2)} PLN")
            print(f"🎴 Wylosowana karta: {pierwsza_karta}")

            self.pokaz_statystyki(pierwsza_karta)
            print(f"{'─' * 60}")

            while True:
                    strzal = input("Następna karta będzie (W)yższa czy (N)iższa? ").strip().upper()
                    if strzal == 'W' or strzal == 'N':
                        break
                    print("Nieprawidłowy wybór! Wpisz W lub N.")
    
            mnoznik = self.oblicz_mnoznik(pierwsza_karta, strzal)

            if mnoznik == 0:
                print("⚠️  Nie można zagrać tą opcją. Wybierz inną.")
                continue
            print(f"🔄 Twój mnożnik to: x{mnoznik}")

            druga_karta = self.talia.dobierz()

            if not druga_karta:
                print("⚠️  Brak kart w talii! Zabierasz obecną wygraną.")
                return aktualna_wygrana
            
            print(f"🎴 Następna karta to: {druga_karta}")

            pierwsza_wartosc = self.wartosc_porownawcza(pierwsza_karta)
            druga_wartosc = self.wartosc_porownawcza(druga_karta)

            if (pierwsza_wartosc == druga_wartosc):
                print("🔄 Remis! Karty mają taką samą wartość. Spróbuj ponownie.")
                continue

            if (strzal == 'W' and druga_wartosc > pierwsza_wartosc) or (strzal == 'N' and druga_wartosc < pierwsza_wartosc):
                aktualna_wygrana = aktualna_wygrana * mnoznik
                print(f"✅ Wygrana! Twoja nowa wygrana to: {round(aktualna_wygrana, 2)} PLN")
                
                kontynuacja = input("Czy chcesz kontynuować grę? (T/N): ").strip().upper()
                if kontynuacja != 'T':
                    print(f"✅ Zabierasz swoją wygraną: {round(aktualna_wygrana, 2)} PLN 💵💵💵")
                    return aktualna_wygrana
                else:
                    continue
            else:
                print("❌ Przegrałeś tę rundę! Tracisz wszystko.")
                aktualna_wygrana = 0
                break
        return aktualna_wygrana