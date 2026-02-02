import random
class Karta:
    '''
    Pojedyncza karta(znak, kolor),
    karta.wartosc - nadana wartość danej karcie w Black Jacku
    '''
    def __init__(self, znak, kolor):
        self.znak = znak
        self.kolor = kolor
    
    def __repr__(self): # tak ma wyświetlac karty
        return f"{self.znak} {self.kolor}"

    @property
    def wartosc(self):
        if self.znak.isdigit():
            return int(self.znak)
        if self.znak in ['J','Q','K']:
            return 10
        if self.znak == 'A':
            return 11 # korekta do 1 przy liczeniu ręki

class Talia:
    '''
    Lista złożona na razie z 52 różnych kart, 
    talia.tasuj() - układa losowo karty w talii, 
    talia.dobierz() - zwraca kartę z talii i ją z niej usuwa
    '''
    def __init__(self):
        kolory = ["Pik", "Kier", "Karo", "Trefl"]
        znaki = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        self.karty = [Karta(z,k) for z in znaki for k in kolory]# na razie 1 talia

    def tasuj(self):
        random.shuffle(self.karty)

    def dobierz(self): # draw
        if len(self.karty)>0:
            return self.karty.pop()
        return None # brak kart w talii
        
class Reka:
    '''
    Karty gracza,
    reka.hit(stos) - bierze kartę ze stosu kart,
    reka.punkty - zwraca wartość punktów na ręcę gracza
    reka.czy_split() - sprawdza warunek splita
    reka.split() - zwraca drugą rękę gracza
    reka.double(stos) - dobiera jedną kartę, podwaja stawkę (ekonomia), zwraca True
    jeśli się udało lub False jeśli nie (gracz nie miał dokładnie dwóch kart na ręcę)
    '''
    def __init__(self):
        self.karty = []
    
    def hit(self, stos: Talia):
        karta=stos.dobierz()
        if karta:
            self.karty.append(karta)


    @property # dla uzywania bez '()'
    def punkty(self):
        suma=0
        asy=0

        for k in self.karty:
            pkt = k.wartosc
            suma=suma+pkt
            if k.znak == "A":
                asy=asy+1
        
        while suma>21 and asy>0:
            suma=suma-10
            asy=asy-1
        
        return suma
    
    def czy_split(self):
        if len(self.karty)!=2:
            return False
        return self.karty[0].wartosc == self.karty[1].wartosc

    def split(self):
        if not self.czy_split():
            print("Do splitu potrzebne dwie równe sobie karty")
            return None
        
        reka2=Reka()
        reka2.karty.append(self.karty.pop())

        return reka2
    
    def double(self,stos:Talia):
        if len(self.karty) == 2:
            self.hit(stos)
            return True
        else:
            return False

    
class Krupier(Reka): # Dziedziczenie klas
    '''
    Modyfikacja ręki na przeciwnika gracza,
    krupier.graj(stos) - krupier dobiera karty dopóki nie ma ponad 16 pkt
    '''
    def graj(self,stos:Talia):
        while self.punkty < 17:
            self.hit(stos)

        # if self.punkty > 21: (mechanika wygrywania)

class Gracz:
    def __init__(self, imie, poczatkowy_balans):
        self.imie = imie
        self.balans = poczatkowy_balans
        self.reka = Reka()
        self.biezacy_zaklad = 0
        self.aktywny_bonus = None # Tu przechowujemy słownik z bonusem

    def postaw_zaklad(self, kwota):
        if 0 < kwota <= self.balans:
            self.biezacy_zaklad = kwota
            self.balans -= kwota
            return True
        return False

    def dodaj_wygrana(self, kwota):
        self.balans += round(kwota, 2)

    
if __name__ == "__main__": #testy, wyswietla sie przy bezpośrednim uruchomieniu, nie przy imporcie
    stos=Talia()
    stos.tasuj()
    hands=[Reka()]
    hands[0].karty.append(Karta('J','Pik'))
    hands[0].karty.append(Karta('10','Kier'))
    
    print(hands[0].karty)
    print(hands[0].punkty)

    hands.append(hands[0].split())

    hands[0].hit(stos)
    hands[1].hit(stos)

    print(hands[0].karty)
    print(hands[0].punkty)
    print(hands[1].karty)
    print(hands[1].punkty)



                
