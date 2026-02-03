LISTA_BONUSOW = {
    1: {"nazwa": "21+3 (Suma oczek = 24)", "mnoznik": 9},
    2: {"nazwa": "Perfect Pair (Para znaków)", "mnoznik": 5},
    3: {"nazwa": "King's Bounty (Dwa Króle)", "mnoznik": 8}, 
    4: {"nazwa": "Krupier Bust (Krupier > 21)", "mnoznik": 3},
    5: {"nazwa": "Holy six seven (Sześć i siedem)", "mnoznik": 67},
    6: {"nazwa": "Super 7 (Same siódemki)", "mnoznik": 15},
    7: {"nazwa": "Super lucky Pięć kart bez busta (bez asa)", "mnoznik": 25},
    8: {"nazwa": "21 ale z przynajmniej 3 kartami", "mnoznik": 2},
    9: {"nazwa": "Para Królewska (Król i dama tego samego znaku)", "mnoznik": 10},
    10:{"nazwa": "Remis z Krupierem", "mnoznik": 4}
}

class ManagerBonusow: 
    def sprawdz_21_plus_3(self, reka_gracza):
        '''
        Sprawdza czy gracz miał 24 punkty na ręce
        '''
        suma_punktow = 0
        for karta in reka_gracza.karty:
            suma_punktow += karta.wartosc
       
        if suma_punktow == 24:
            return True
        else:
            return False

    def sprawdz_perfect_pair(self, reka_gracza):
        '''
        Sprawdza czy na ręce gracza znajdują się dwie karty 
        o tym samym znaku.
         '''
        widziane_znaki = []
        
        for karta in reka_gracza.karty:
           
            if karta.znak in widziane_znaki:
                return True 
            widziane_znaki.append(karta.znak)
            
        return False
    def sprawdz_kings_bounty(self, reka_gracza):
        '''
        Sprawdza czy na ręce gracza znajdują się dwie karty 
        o wartości Króla
         '''
        liczba_kroli = 0
        
        for karta in reka_gracza.karty:
            if karta.wartosc == 10 and karta.znak == 'K':
                liczba_kroli += 1
                
        if liczba_kroli == 2:
            return True
        else:
            return False
    def sprawdz_krupier_bust(self, karta_krupiera):
        '''
        Sprawdza czy krupier przekroczył 21 punktów
        '''
        suma_punktow = 0
        
        for karta in karta_krupiera.karty:
            suma_punktow += karta.wartosc
            
        if suma_punktow > 21:
            return True
        else:
            return False
    def sprawdz_holy_six_seven(self, reka_gracza):
        '''
        Sprawdza czy na ręce gracza znajdują się karty o wartościach 6 i 7
        '''
        for i in range(len(reka_gracza.karty)-1):
            if  reka_gracza.karty[i].wartosc== 6 and reka_gracza.karty[i+1].wartosc== 7:
                return True
        return False
    def sprawdz_super_7(self, reka_gracza):
        '''
        Sprawdza czy na ręce gracza znajdują się same siódemki
        '''
        for karta in reka_gracza.karty:
            if karta.wartosc != 7:
                return False
        if len(reka_gracza.karty) == 3:
            return True
        return False
    def sprawdz_piec_kart_bez_busta(self, reka_gracza):
        '''
        Sprawdza czy gracz ma pięć kart i nie przekroczył 21 punktów
        '''
        if len(reka_gracza.karty) == 5:
            suma_punktow = 0
            for karta in reka_gracza.karty:
                suma_punktow += karta.wartosc
            if suma_punktow <= 21:
                return True
        return False
    def sprawdz_21_ale_bez_black_jacka(self, reka_gracza):
        '''
        Sprawdza czy gracz ma 21 punktów, ale ma wiecej niż dwie karty
        '''
        suma_punktow_gracza = 0
        for karta in reka_gracza.karty:
            suma_punktow_gracza += karta.wartosc
        if suma_punktow_gracza == 21  and not len(reka_gracza.karty) == 2:
            return True
        else:
            return False
    def sprawdz_para_krolewska(self, reka_gracza):
        '''
        Sprawdza czy na ręce gracza znajdują się karty o wartościach Króla i Damy tego samego znaku
        '''
        krol_znaki = []
        dama_znaki = []
        
        for karta in reka_gracza.karty:
            if karta.wartosc == 10 and karta.znak == 'K':
                krol_znaki.append(karta.znak)
            elif karta.wartosc == 10 and karta.znak == 'Q':
                dama_znaki.append(karta.znak)
        
        for znak in krol_znaki:
            if znak in dama_znaki:
                return True
        return False
    def sprawdz_remis_z_krupierem(self, reka_gracza, reka_krupiera):
        '''
        Sprawdza czy gracz ma remis z krupierem
        '''
        suma_punktow_gracza = 0
        suma_punktow_krupiera = 0
        
        for karta in reka_gracza.karty:
            suma_punktow_gracza += karta.wartosc
            
        for karta in reka_krupiera.karty:
            suma_punktow_krupiera += karta.wartosc
            
        if suma_punktow_gracza == suma_punktow_krupiera:
            return True
        else:
            return False
        
    def rozlicz_zaklad(self, zaklad, reka_gracza, karta_krupiera):
        '''Główna funkcja, która sprawdza czy zakład wygrał i zwraca kwotę wygranej.
        Jeśli przegrał, zwraca 0.
        '''
        if zaklad is None:
            return 0
        
        id_bonus = zaklad['id']
        stawka = zaklad['stawka']
        wygrana = 0
        czy_sukces = False
    

        
        
        if id_bonus == 1: 
            czy_sukces = self.sprawdz_21_plus_3(reka_gracza)
            
        elif id_bonus == 2: 
            czy_sukces = self.sprawdz_perfect_pair(reka_gracza)
        elif id_bonus == 3: 
            czy_sukces = self.sprawdz_kings_bounty(reka_gracza)
        elif id_bonus == 4: 
            czy_sukces = self.sprawdz_krupier_bust(karta_krupiera)
        elif id_bonus == 5:
            czy_sukces = self.sprawdz_holy_six_seven(reka_gracza)
        elif id_bonus == 6:
            czy_sukces = self.sprawdz_super_7(reka_gracza)
        elif id_bonus == 7:
            czy_sukces = self.sprawdz_piec_kart_bez_busta(reka_gracza)
        elif id_bonus == 8:
            czy_sukces = self.sprawdz_21_ale_bez_black_jacka(reka_gracza)
        elif id_bonus == 9:
            czy_sukces = self.sprawdz_para_krolewska(reka_gracza)
        elif id_bonus == 10:
            czy_sukces = self.sprawdz_remis_z_krupierem(reka_gracza, karta_krupiera)
        
        if czy_sukces:
            mnoznik = LISTA_BONUSOW[id_bonus]['mnoznik']
            wygrana = stawka * mnoznik
            print(f"\n$$$ BONUS TRAFIONY! Wygrywasz {wygrana} (Mnożnik x{mnoznik}) $$$")
            return wygrana
        else:
            print(f"\nBonus {LISTA_BONUSOW[id_bonus]['nazwa']} nietrafiony. Tracisz {stawka}.")
            return 0