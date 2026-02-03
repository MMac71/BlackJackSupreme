# BlackJackSupreme
Projekt zaliczeniowy kursu "Wstęp do programowania"

**Temat projektu:** Gra w Blackjack
**Autorzy:**
1. Wojciech Czech 293182
2. Maciej Maciejko 293181
3. Franciszek Świerczewski 293398
4. Dawid Marszałek 293157

---

## Zasady gry

1. **Cel gracza**
   * Celem gracza jest pokonanie krupiera. Można to zrobić na dwa sposoby:
     * Mieć wyższą sumę punktów niż krupier.
     * Sprawić, by krupier przekroczył 21 punktów, gdy nadal jesteś w grze.

2. **Wartości kart**
   * Karty 2-9: mają wartość zgodną z liczbą.
   * 10, Walet (J), Dama (Q), Król (K): wszystkie mają wartość 10 pkt.
   * As (A): liczony jako 1 lub 11, w zależności od tego, co jest lepsze dla gracza.
   > **Przykład:** As + 6 to tzw. "miękkie 17". Możesz dobrać kartę. Jeśli dobierzesz 10, As zmienia wartość na 1, żebyś nie przegrał (masz wtedy 17, a nie 27).

3. **Decyzje gracza**
   * **Podstawowe ruchy:**
     * **Hit (Dobieranie karty):** Prosisz o kolejną kartę. Robisz to, gdy masz mało punktów i chcesz zbliżyć się do 21.
     * **Stand (Pas):** Nie bierzesz więcej kart. Zostajesz z tym, co masz i czekasz na ruch krupiera.
   * **DOUBLE DOWN (Podwojenie stawki):**
     * Podwajasz swój pierwotny zakład (dokładasz drugie tyle żetonów), ale w zamian otrzymujesz dokładnie jedną kartę. Po niej kończysz turę (automatyczny Stand).
   * **SPLIT (Rozdzielenie):**
     * Rozdzielasz karty na dwie osobne ręce. Musisz dołożyć drugi zakład (równy pierwszemu) dla nowej ręki. Od teraz grasz dwiema niezależnymi rękami przeciwko krupierowi.

4. **Zasady krupiera**
   * Krupier gra według ustalonego schematu:
     * Musi dobierać karty (Hit), dopóki ma 16 punktów lub mniej.
     * Musi spasować (Stand), gdy ma 17 punktów lub więcej.

5. **Bonusy (Side Bets)**
   * Gracz przed rozpoczęciem każdej rundy może postawić zakład na bonus.
   * **Rodzaje bonusów:**
     * **21+3 (Suma 24):** Twoja suma punktów wynosi dokładnie 24. Wypłata 9:1.
     * **Perfect Pair:** Musisz posiadać dwie karty o tym samym znaku. Wypłata 5:1.
     * **King's Bounty:** Posiadanie dwóch Króli na ręce. Wypłata 8:1.
     * **Krupier Bust:** Krupier przekroczy 21 punktów. Wypłata 3:1.
     * **Holy Six Seven:** Masz w ręce szóstkę i siódemkę. Wypłata 67:1.
     * **Super 7:** Twoja ręka musi składać się z samych siódemek. Wypłata 15:1.
     * **Super Lucky:** 5 kart w ręce bez przekroczenia 21 punktów. Wypłata 25:1.
     * **21 (3+ karty):** Uzyskanie sumy 21 przy użyciu co najmniej trzech kart. Wypłata 2:1.
     * **Para Królewska:** Posiadanie Króla i Damy tego samego znaku. Wypłata 10:1.
     * **Remis z Krupierem:** Twój wynik jest taki sam jak krupiera. Wypłata 4:1.

6. **Wynik**
   * **Blackjack:** As + karta za 10 pkt (10, J, Q, K) w pierwszych dwóch kartach. Wypłata 3:2.
   * **Wygrana:** Masz więcej niż krupier lub krupier przekroczył 21. Wypłata 1:1.
   * **Push:** Masz tyle samo punktów co krupier. Odzyskujesz swój zakład.
   * **Bust:** Przekroczyłeś 21 punktów. Przegrywasz od razu, nawet jeśli krupier później też przekroczy 21.
