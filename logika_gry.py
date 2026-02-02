from bonusy import LISTA_BONUSOW
from pobieranie_decyzji import pobierz_akcje
from wyświetlanie_na_ekran import wyswietl_stan_gry

def pobierz_zaklad(gracz):
    while True:
        try:
            kwota = float(input(f"Twój balans: {gracz.balans} PLN. Ile stawiasz? "))
            if gracz.postaw_zaklad(kwota):
                return kwota
            print("❌ Masz za mało pieniędzy!")
        except ValueError:
            print("❌ Podaj poprawną liczbę.")

def obsluga_bonusow(gracz):
    print("\n--- BONUSY SIDE-BET ---")
    for k, v in LISTA_BONUSOW.items():
        print(f"{k}. {v['nazwa']} (x{v['mnoznik']})")
    
    wybor_b = input("Czy chcesz postawić na bonus? (Podaj nr lub Enter by pominąć): ")
    
    if wybor_b.isdigit() and int(wybor_b) in LISTA_BONUSOW:
        id_bonusu = int(wybor_b)
        try:
            stawka_b = float(input(f"Ile stawiasz na bonus '{LISTA_BONUSOW[id_bonusu]['nazwa']}'? "))
            if stawka_b > 0 and stawka_b <= gracz.balans:
                gracz.balans -= stawka_b
                gracz.aktywny_bonus = {'id': id_bonusu, 'stawka': stawka_b}
                print("✅ Zakład na bonus przyjęty.")
            else:
                print("❌ Za mało środków na bonus lub błędna kwota.")
        except ValueError:
            print("❌ Błąd wprowadzania kwoty.")

def rozegraj_pojedyncza_reke(gracz, krupier, talia, numer_reki=1):
    while gracz.reka.punkty < 21:
        print(f"\n--- GRANIE RĘKĄ NR {numer_reki} ---")
        wyswietl_stan_gry(gracz, krupier)
        decyzja = pobierz_akcje(gracz, talia)
        
        if decyzja == 'HIT':
            gracz.reka.hit(talia)
            print(f"➡️ Dobierasz: {gracz.reka.karty[-1]}")
        elif decyzja == 'STAND':
            print("➡️ Pasujesz.")
            break
        elif decyzja == 'DOUBLE':
            print("➡️ DOUBLE DOWN!")
            gracz.reka.hit(talia)
            break
        elif decyzja == 'SPLIT':
            print("⚠️ Split dostępny tylko przy pierwszym ruchu w turze!")

def tura_gracza(gracz, krupier, talia):
    if gracz.reka.czy_split():
        wyswietl_stan_gry(gracz, krupier)
        print("Masz parę! Czy chcesz zrobić SPLIT? (kosztuje drugą stawkę)")
        decyzja = input("Wpisz 'P' aby zrobić Split, cokolwiek innego by grać dalej: ").upper()
        
        if decyzja == 'P':
            if gracz.balans >= gracz.biezacy_zaklad:
                print("🔀 Wykonujesz SPLIT!")
                gracz.balans -= gracz.biezacy_zaklad 
                
                reka1 = gracz.reka
                reka2 = gracz.reka.split()
                
                reka1.hit(talia)
                reka2.hit(talia)
                
                gotowe_rece = []

                rozegraj_pojedyncza_reke(gracz, krupier, talia, numer_reki=1)
                gotowe_rece.append(reka1)

                gracz.reka = reka2 
                rozegraj_pojedyncza_reke(gracz, krupier, talia, numer_reki=2)
                gotowe_rece.append(reka2)
                
                return gotowe_rece
            else:
                print("❌ Nie stać Cię na Split.")

    rozegraj_pojedyncza_reke(gracz, krupier, talia)
    return [gracz.reka]

def tura_krupiera(lista_rak_gracza, krupier, talia):
    wszystkie_fura = True
    for reka in lista_rak_gracza:
        if reka.punkty <= 21:
            wszystkie_fura = False
            break
            
    if not wszystkie_fura:
        print("\n--- RUCH KRUPIERA ---")
        krupier.graj(talia)
    else:
        print("\nWszystkie Twoje ręce przekroczyły 21. Krupier nie musi grać.")

def rozlicz_blackjacka(gracz, krupier, lista_rak):
    punkty_k = krupier.punkty
    stawka_pojedyncza = gracz.biezacy_zaklad
    laczna_wygrana = 0

    print(f"\n{'='*15} WYNIKI KOŃCOWE {'='*15}")
    print(f"🃏 Krupier ma: {punkty_k}")

    for i, reka in enumerate(lista_rak, 1):
        punkty_g = reka.punkty
        print(f"\n--- Ręka #{i} ({reka.karty}) ---")
        
        wygrana_reki = 0
        if punkty_g > 21:
            print(f"❌ FURA! ({punkty_g}). Tracisz stawkę.")
        elif punkty_k > 21:
            wygrana_reki = stawka_pojedyncza * 2
            print(f"✅ Krupier Fura! Wygrywasz {wygrana_reki} PLN.")
        elif punkty_g > punkty_k:
            wygrana_reki = stawka_pojedyncza * 2
            print(f"✅ WYGRANA! {punkty_g} vs {punkty_k}. +{wygrana_reki} PLN.")
        elif punkty_g == punkty_k:
            wygrana_reki = stawka_pojedyncza
            print(f"🔄 REMIS. Zwrot {wygrana_reki} PLN.")
        else:
            print(f"❌ PRZEGRANA. {punkty_g} vs {punkty_k}.")
            
        laczna_wygrana += wygrana_reki

    return laczna_wygrana

def obsluga_minigry(gracz, zysk_netto, gra_minigra):
    if zysk_netto > 0:
        print(f"\n🎰 Wygrałeś łącznie {zysk_netto} PLN na czysto.")
        decyzja = input("Chcesz zaryzykować tę kwotę w Wyższa/Niższa? (T/N): ").upper()
        if decyzja == 'T':
            gracz.balans -= zysk_netto 
            finalna_wygrana = gra_minigra.graj(zysk_netto)
            gracz.dodaj_wygrana(finalna_wygrana)
        else:
            print("Pieniądze trafiają na konto.")