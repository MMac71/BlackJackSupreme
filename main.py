from karty import Talia, Reka, Krupier
from bonusy import LISTA_BONUSOW, ManagerBonusow
from mini_gra import nizsza_wyzsza

def wyswietl_reke(reka, ukryj_pierwsza=False):
    """Wyświetla karty w ręce"""
    if ukryj_pierwsza:
        print(f"[UKRYTA], {reka.karty[1]}")
    else:
        print(", ".join(str(k) for k in reka.karty), f"(Punkty: {reka.punkty})")

def pokaz_bonusy():
    """Wyświetla dostępne bonusy"""
    print("\n" + "="*60)
    print("DOSTĘPNE BONUSY:")
    print("="*60)
    for id_bonus, info in LISTA_BONUSOW.items():
        print(f"{id_bonus}. {info['nazwa']} - Mnożnik x{info['mnoznik']}")
    print("="*60)

def wybierz_bonus(saldo):
    """Pozwala graczowi wybrać i postawić na bonus"""
    pokaz_bonusy()
    
    wybor = input("\nCzy chcesz postawić na bonus? (T/N): ").strip().upper()
    if wybor != 'T':
        return None
    
    while True:
        try:
            id_bonus = int(input("Wybierz numer bonusu (1-10): "))
            if id_bonus not in LISTA_BONUSOW:
                print("Nieprawidłowy numer bonusu!")
                continue
            
            stawka = float(input(f"Ile chcesz postawić na bonus? (Max: {saldo}): "))
            if stawka <= 0 or stawka > saldo:
                print("Nieprawidłowa stawka!")
                continue
            
            return {'id': id_bonus, 'stawka': stawka}
        except ValueError:
            print("Podaj prawidłową wartość!")

def graj_runde(stos, saldo):
    """Jedna runda blackjacka"""
    print("\n" + "="*60)
    print(f"💰 Twoje saldo: {saldo} PLN")
    print("="*60)
    
    # Postawienie zakładu głównego
    while True:
        try:
            zaklad = float(input("Postaw zakład: "))
            if zaklad <= 0 or zaklad > saldo:
                print("Nieprawidłowa stawka!")
                continue
            break
        except ValueError:
            print("Podaj prawidłową wartość!")
    
    # Wybór bonusu
    bonus_zaklad = wybierz_bonus(saldo - zaklad)
    if bonus_zaklad:
        saldo -= bonus_zaklad['stawka']
    
    # Rozdanie kart
    reka_gracza = Reka()
    krupier = Krupier()
    
    for _ in range(2):
        reka_gracza.hit(stos)
        krupier.hit(stos)
    
    print("\n--- TWOJE KARTY ---")
    wyswietl_reke(reka_gracza)
    print("\n--- KARTY KRUPIERA ---")
    wyswietl_reke(krupier, ukryj_pierwsza=True)
    
    # Blackjack gracza
    if reka_gracza.punkty == 21:
        print("\n🎉 BLACKJACK! 🎉")
        wygrana = zaklad * 2.5
    else:
        # Tura gracza
        while reka_gracza.punkty < 21:
            akcja = input("\n(H)it, (S)tand, (D)ouble, S(p)lit? ").strip().upper()
            
            if akcja == 'H':
                reka_gracza.hit(stos)
                print("--- TWOJE KARTY ---")
                wyswietl_reke(reka_gracza)
            elif akcja == 'S':
                break
            elif akcja == 'D':
                if reka_gracza.double(stos):
                    zaklad *= 2
                    print(f"Double! Nowy zakład: {zaklad}")
                    print("--- TWOJE KARTY ---")
                    wyswietl_reke(reka_gracza)
                    break
                else:
                    print("Nie możesz użyć double!")
            elif akcja == 'P':
                if reka_gracza.czy_split():
                    print("Split jest możliwy, ale wymaga dodatkowej implementacji!")
                else:
                    print("Nie możesz użyć split!")
        
        # Sprawdzenie czy gracz nie zbustował
        if reka_gracza.punkty > 21:
            print("\n❌ BUST! Przegrałeś!")
            wygrana = 0
        else:
            # Tura krupiera
            print("\n--- KRUPIER GRA ---")
            krupier.graj(stos)
            wyswietl_reke(krupier)
            
            # Rozstrzygnięcie
            if krupier.punkty > 21:
                print("\n✅ Krupier BUST! Wygrywasz!")
                wygrana = zaklad * 2
            elif reka_gracza.punkty > krupier.punkty:
                print("\n✅ Wygrywasz!")
                wygrana = zaklad * 2
            elif reka_gracza.punkty == krupier.punkty:
                print("\n🤝 Remis!")
                wygrana = zaklad
            else:
                print("\n❌ Krupier wygrywa!")
                wygrana = 0
    
    # Rozliczenie bonusu
    manager_bonusow = ManagerBonusow()
    wygrana_bonus = manager_bonusow.rozlicz_zaklad(bonus_zaklad, reka_gracza, krupier)
    
    # Aktualizacja salda
    nowe_saldo = saldo - zaklad + wygrana + wygrana_bonus
    
    print(f"\n💰 Wygrana: {wygrana} PLN")
    if wygrana_bonus > 0:
        print(f"💰 Wygrana z bonusu: {wygrana_bonus} PLN")
    print(f"💰 Nowe saldo: {nowe_saldo} PLN")
    
    # Mini-gra wyższa/niższa
    if wygrana > 0:
        gra_wn = nizsza_wyzsza(stos)
        koncowa_wygrana = gra_wn.graj(wygrana)
        nowe_saldo = saldo - zaklad + koncowa_wygrana + wygrana_bonus
    
    return nowe_saldo

def main():
    print("="*60)
    print("🎰  WITAJ W BLACKJACK! 🎰")
    print("="*60)
    
    saldo = 1000.0
    
    while saldo > 0:
        stos = Talia()
        stos.tasuj()
        
        saldo = graj_runde(stos, saldo)
        
        if saldo <= 0:
            print("\n❌ Koniec gry! Nie masz już środków!")
            break
        
        kontynuuj = input("\nCzy chcesz zagrać kolejną rundę? (T/N): ").strip().upper()
        if kontynuuj != 'T':
            print(f"\n✅ Dziękujemy za grę! Twoje końcowe saldo: {saldo} PLN")
            break

if __name__ == "__main__":
    main()