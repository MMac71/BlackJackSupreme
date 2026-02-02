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

5. **Bonusy**
   * *(Do uzupełnienia)*

6. **Wynik**
   * **Blackjack:** As + karta za 10 pkt (10, J, Q, K) w pierwszych dwóch kartach. Wypłata 3:2.
   * **Wygrana:** Masz więcej niż krupier lub krupier przekroczył 21. Wypłata 1:1.
   * **Push:** Masz tyle samo punktów co krupier. Odzyskujesz swój zakład.
   * **Bust:** Przekroczyłeś 21 punktów. Przegrywasz od razu, nawet jeśli krupier później też przekroczy 21.
