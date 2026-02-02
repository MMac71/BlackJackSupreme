def wyswietl_stan_gry(gracz, krupier, zakonczona=False):
    """
    Wyświetla stan stołu, saldo oraz bieżący zakład.
    gracz: obiekt klasy Gracz (posiadający balans, zaklad i reke)
    krupier: obiekt klasy Krupier
    """
    print("\n" + "═"*45)
    print(f" PORTFEL: ${gracz.balans:<10} BIEŻĄCY ZAKŁAD: ${gracz.zaklad}")
    print("─"*45)
    
    # Wyświetlanie kart krupiera
    if zakonczona:
        print(f" KRUPIER: {krupier.karty} (Suma: {krupier.punkty})")
    else:
        # Sprawdzamy czy krupier ma karty, żeby uniknąć błędu przy pustej ręce
        karta_widoczna = krupier.karty[0] if krupier.karty else "?"
        print(f" KRUPIER: [{karta_widoczna}, ?]")
    
    print("-" * 25)
    
    # Wyświetlanie kart gracza
    print(f" TWOJA RĘKA: {gracz.reka.karty} (Suma: {gracz.reka.punkty})")
    print("═"*45 + "\n")