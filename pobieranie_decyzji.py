from obiekty import Talia
from obiekty import Gracz

def pobierz_akcje(gracz: Gracz, stos: Talia):
    opcje = ["(H) Hit", "(S) Stand"]
    
    # Możliwość podwojenia (tylko 2 karty i odpowiednie saldo)
    mozna_double = len(gracz.reka.karty) == 2 and gracz.balans >= gracz.biezacy_zaklad
    if mozna_double:
        opcje.append("(D) Double Down")
        
    print(f"DOSTĘPNE AKCJE: {', '.join(opcje)}")
    
    while True:
        wybor = input("Wybierz akcję: ").upper()
        if wybor == 'H': return 'HIT'
        if wybor == 'S': return 'STAND'
        if wybor == 'D' and mozna_double:
            gracz.balans -= gracz.biezacy_zaklad
            gracz.biezacy_zaklad *= 2
            return 'DOUBLE'
        if wybor == 'P':
            return 'SPLIT'
        print("❌ Nieprawidłowy wybór!")