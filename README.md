# 🐍 Gra w Węża (Snake Game)

Gra w węża zrealizowana za pomocą Pythona i biblioteki Pygame. 
Gracz steruje wężem, który porusza się po planszy. Celem gry jest zjadanie pojawiającego się 
jedzenia, co powoduje wydłużenie węża. Gra kończy się, gdy wąż zjada samego siebie.

## 📋 Wymagania

- Python 3.10 lub nowszy
- Pygame

## 💻 Instalacja i 🚀 Uruchomienie gry

1. Klonuj repozytorium:

```basz
git clone https://github.com/sebastianLedzianowski/snake_game.git
```

2. Przejdź do katalogu projektów:

```basz
cd snake_game
```

3. Skonfiguruj środowisko wirtualne i aktywuj je (opcjonalnie, ale zalecane):

```basz
virtualenv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Zainstaluj zależności za pomocą pliku `requirements.txt`:

```basz
pip install -r requirements.txt
```

5. Uruchom gre:

```basz
python game.py
```

## 🎮 Sterowanie

- Strzałka w lewo: skręć w lewo
- Strzałka w prawo: skręć w prawo
- Strzałka w górę: skręć w górę
- Strzałka w dół: skręć w dół

## ✨ Funkcje gry

- Poruszanie się węża w czterech kierunkach
- Zjadanie jedzenia powoduje wydłużenie węża
- Gra kończy się, gdy wąż uderzy w samego siebie
- Po każdym zjedzonym jedzeniu, losowo pojawia się nowe jedzenie na planszy

## 📈 Rozwój gry

Gra jest w trakcie rozwoju. Planowane są następujące funkcje:
- Ekran startowy i ekran końca gry
- Tworzenie menu opcji
- Tabele wyników
- Poziomy trudności
- Dodanie bonusów i przeszkód
- Implementacja pauzy w grze
- Wprowadzenie różnych trybów gry

## 👨‍💻 Autor

- [Sebastian Ledzianowski](https://github.com/sebastianLedzianowski)


## ⚖️ Licencja

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE), aby uzyskać szczegółowe informacje.

## 💖 Podziękowania

Chciałbym serdecznie podziękować wszystkim, którzy w jakikolwiek sposób przyczynili się do powstania tej gry.

Specjalne podziękowania dla:
- Marcina Moskały, autora książki ["Python od podstaw. Zacznij swoją przygodę z programowaniem"](https://lubimyczytac.pl/ksiazka/5032864/python-od-podstaw-zacznij-swoja-przygode-z-programowaniem), za dostarczenie solidnych fundamentów i inspiracji do nauki programowania i tworzenia gier w Pythonie.
- Społeczności Pygame za rozwijanie i utrzymanie tak potężnej biblioteki, która umożliwia łatwe tworzenie gier w Pythonie.
- Każdej osobie z forum `r/pygame` na Reddit i użytkownikom Stack Overflow za ich bezcenne porady i wskazówki, które pomogły mi przezwyciężyć wiele trudności.
- Moim przyjaciołom i rodzinie za ich wsparcie i motywację do ciągłego rozwijania moich umiejętności programistycznych.

Ten projekt nie byłby możliwy bez wsparcia i zachęty od tak wielu niesamowitych ludzi. Dziękuję!
