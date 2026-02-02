from obiekty import Gracz
from obiekty import Krupier
from bonusy import LISTA_BONUSOW

def wyswietl_stan_gry(gracz: Gracz, krupier: Krupier, zakonczona=False):

    print("\n" + "═" * 50)
    print(f"👤 GRACZ: {gracz.imie:<15} 💰 SALDO: {gracz.balans} PLN")
    print(f"💵 ZAKŁAD: {gracz.biezacy_zaklad} PLN")
    if gracz.aktywny_bonus:
        print(f"✨ BONUS: {LISTA_BONUSOW[gracz.aktywny_bonus['id']]['nazwa']}")
    print("─" * 50)

    # Sekcja Krupiera
    if zakonczona:
        print(f"🃏 KRUPIER: {krupier.karty} (Suma: {krupier.punkty})")
    else:
        widoczna = krupier.karty[0] if krupier.karty else "Brak"
        print(f"🃏 KRUPIER: [{widoczna}, ?]")

    print("-" * 20)

    # Sekcja Gracza
    print(f"🎴 TWOJE KARTY: {gracz.reka.karty} (Suma: {gracz.reka.punkty})")
    print("═" * 50 + "\n")