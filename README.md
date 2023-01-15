# System szacowania ceny wynajmu mieszkań

[Link do formularza](http://chomicz.pythonanywhere.com/)


## Charakterystyka oprogramowania

Przedstawiony poniżej projekt dotyczy systemu szacowania miesięcznej ceny wynajmu mieszkań w Gdańsku.

Projekt zakłada przygotowanie oprogramowania pozwalającego użytkownikowi na oszacowanie przeciętnego kosztu wynajmu lokalu na obszarze miasta Gdańsk. Koszt estymowany jest modelem predykcyjnym na podstawie parametrów opartych na istniejących ofertach najmu pozyskanych z internetowego portalu ogłoszeniowego. Poprzez aplikację webową użytkownik może wprowadzić warianty zdefiniowanych wcześniej parametrów lokalu, aby otrzymać oszacowany średni miesięczny koszt wynajmu.

Oprogramowanie składa się z trzech części:
1. Program pobierający dane z sieci internetowej - wykorzystuje algorytm typu web scraping do pozyskania szczegółów ofert wynajmu publikowanych na portalu https://ogloszenia.trojmiasto.pl/.
2. Program estymujący model – oczyszcza i konwertuje dane z punktu pierwszego, następnie szacuje na ich podstawie model regresji liniowej metodą najmniejszych kwadratów.
3. Aplikacja webowa – stanowi graficzny interfejs użytkownika, zapewniając miejsce do wprowadzenia wariantów parametrów estymacji, aby następnie wyświetlić wynik oszacowania przeciętnej miesięcznej ceny najmu.

## Prawa autorskie
#### Autorzy

Copyright (c) 2023, Dawid Chomicz, Małgorzata Góra, Paweł Błaszkowski

#### Warunki licencyjne

Oprogramowanie zostało udostępnione na licencji BSD 3-klauzulowej, o następującej treści:

Redystrybucja i wykorzystanie w formie źródłowej i binarnej, z modyfikacjami lub bez, jest dozwolone pod warunkiem spełnienia następujących warunków:

1. Redystrybucja kodu źródłowego musi zawierać powyższą informację o prawach autorskich, niniejszą listę warunków i poniższe zastrzeżenie.
2. Redystrybucje w formie binarnej muszą odtwarzać powyższą informację o prawach autorskich, niniejszą listę warunków i poniższe zastrzeżenie w dokumentacji i/lub innych materiałach dostarczanych z dystrybucją.
3. Nazwisko właściciela praw autorskich, ani nazwiska jego współtwórców nie mogą być używane do popierania lub promowania produktów pochodzących z tego oprogramowania bez wyraźnej uprzedniej pisemnej zgody.

Treść oryginalnej licencji oraz zastrzeżenia w wersji angielskiej można znaleźć w załączonym pliku LICENSE.md.

## Specyfikacja wymagań

| Id | Nazwa | Opis | Priorytet <br />[1 - wymagane, 2 - przydatne, 3 – opcjonalne] | Kategoria  
|:---:|:---:|:---:|:---:|:---:
|1|Ustawienie parametrów przez użytkownika|Użytkownik może wskazać wartości poszczególnych parametrów lokalu|1|funkcjonalne  
|2|Parametry kategoryczne w formie listy rozwijanej|Użytkownik może wybrać warianty parametrów kategorycznych jako jeden z elementów listy rozwijanej|2|funkcjonalne
|3|Podanie powierzchni jako liczbę całkowitą|Użytkownik może wprowadzić parametr „Powierzchnia lokalu” do pola wejściowego jako dowolną liczbę całkowitą dodatnią|1|funkcjonalne
|4|Zwracanie komunikatów użytkownikowi|W przypadku wpisania niepoprawnej wartości w polu „Powierzchnia lokalu” system powinien zwracać odpowiedni komunikat|2|funkcjonalne
|5|Ustawienie wybranych parametrów przez użytkownika|Użytkownik ma możliwość uzupełnienia wybranych parametrów, przy pozostawieniu pozostałych jako puste|3|funkcjonalne
|6|Dokonanie obliczeń po kliknięciu przycisku|Po kliknięciu przycisku „Oblicz” system powinien wykonać oszacowanie ceny wynajmu na podstawie wprowadzonych przez użytkownika parametrów|1|funkcjonalne
|7|Zwrócenie wyniku po kliknięciu przycisku|Załadowana po kliknięciu przycisku „Oblicz” podstrona powinna pokazywać wynik estymacji w formie liczby zmiennoprzecinkowej z dokładnością do części setnych i walutą, w jakiej została wyliczona|1|funkcjonalne
|8|Wybór lokalizacji|Użytkownik może wybrać dowolne miasto, dla którego chce mieć zwrócony wynik|3|funkcjonalne
|9|Wielokrotny wybór dla parametrów|Użytkownik może zaznaczyć kilka wariantów danego parametru jednocześnie|3|funkcjonalne
|10|Czas trwania obliczeń|Podstrona powinna się ładować w ciągu maksymalnie 10. sekund od kliknięcia przycisku „Oblicz”|2|funkcjonalne
|11|Dostępność strony|Aplikacja ma być dostępna na serwerze całą dobę każdego dnia w okresie funkcjonowania (3 mies.)|1|niefunkcjonalne
|12|Ograniczenie liczby użytkowników|Z aplikacji jednocześnie może korzystać maksymalnie 10 użytkowników|2|niefunkcjonalne
|13|Zgłaszanie problemów z działaniem strony|Użytkownicy mogą zgłaszać problemy z funkcjonowaniem aplikacji na podany na stronie adres mailowy support@example.com|3|niefunkcjonalne
|14|Wyświetlane elementy aplikacji|Aplikacja wyświetla takie elementy jak: tekst, nagłówki, pola wyboru z listą rozwijaną, numeryczne pole wejściowe, przycisk zatwierdzający|1|niefunkcjonalne
|15|Oprawa graficzna|Aplikacja jest oprawiona nowoczesną szatą graficzną|3|niefunkcjonalne
|16|Responsywność|Aplikacja jest responsywna i dostosowuje się do wielkości okna przeglądarki|2|niefunkcjonalne


## Architektura systemu

### Wykorzystane technologie

1. Środowisko programistyczne
   - Anaconda Distribution
   - Jupyter Notebook
   - Jupyter Lab
2. Język programowania Python wersja 3.8.3
3. Biblioteki i pakiety języka Python:
   - **pandas** wersja 1.5.2
   - **numpy** wersja 1.24.1
   - **matplotlib** wersja 3.6.3
   - **statsmodels** wersja 0.13.5
   - **Flask** wersja 2.2.2
   - **requests** wersja 2.26.0
   - **bs4 > BeautifulSoup** wersja 4.10.0
   - **urllib.request > Request** wersja 3.9
4. Platforma hostingowa PythonAnywhere


### Przebieg działania programu pobierającego informacje o ofertach wynajmu
1. Programista określa w systemie bazowy (wyjściowy) adres URL strony, z której mają zostać pobrane informacje oraz numer strony, od której system rozpocznie wyszukiwanie.
2. System wysyła zapytanie do wskazanej strony wyjściowej wraz z określonymi nagłówkami żądania (headers), w tym: “User-Agent” oraz “Referer”.
3. System pobiera kod HTML ze wskazanej strony.
4. System pobiera numer ostatniej strony wyników wyszukiwania ze strony bazowej.
5. System przechodzi przez kolejne strony wyników wyszukiwania, kończąc na ostatniej, i z każdej z nich pobiera linki do wszystkich ofert, znajdujących się na danej stronie.
6. Przed przejściem na kolejną stronę system czeka od 2 do 10 sekund, żeby nie przeciążać portalu nadmiarową ilością wysyłanych żądań w krótkim czasie. 
7. Pobrane linki ofert system zapisuje w liście.
8. System pobiera kolejno ze wszystkich ofert z listy informacje na temat ceny wynajmu oraz wszelkich innych szczegółów oferty. 
9. Przed przejściem do kolejnej oferty system czeka od 2 do 10 sekund, żeby nie przeciążać portalu nadmiarową ilością wysyłanych żądań w krótkim czasie. 
10. Ze względu na zróżnicowanie dostępnych dla użytkowników portalu szczegółów oferty (oferty mogą mieć różne pola wyszczególnione, nie ma jednej określonej struktury) system pobiera informacje o wszystkich możliwych polach, jakie oferta może zawierać. W przypadku gdy oferta nie posiada informacji na temat danego pola, system pole to pomija.
11. System zapisuje pobrane informacje z danej oferty w słowniku.
12. Słownik ten system następnie konwertuje na ramkę danych.
13. System zlicza w międzyczasie oferty, jakie zostały już przez niego przetworzone. 
14. Po pobraniu danych z ofert, których liczba jest wielokrotnością liczby 100, system zwraca informację o przetworzeniu danej liczby ofert z liczby wszystkich dostępnych i zapisuje otrzymane w ramce danych wyniki w pliku .csv we wskazanym do tego miejscu. Dzieje się to w ramach zabezpieczenia przed utratą danych w przypadku na przykład utraty połączenia z siecią.
15. W przypadku gdy dana oferta zostanie usunięta bądź zostanie oznaczona jako nieaktualna przed próbą pobrania informacji na jej temat, system zwróci informację o błędzie i poda link do oferty, której danych nie udało się pobrać. Następnie pominie daną ofertą i przejdzie do kolejnej.
16. Po pobraniu wszystkich informacji o wszystkich aktualnych ofertach, system zwraca wyniki zapisane w ramce danych w postaci pliku .csv zapisanego we wskazanym do tego miejscu na dysku.

### Przebieg działania programu estymującego model predykcyjny
1. System akceptuje dane wejściowe w postaci pliku .csv.
2. System konwertuje wprowadzony zbiór danych na obiekt typu ramka danych.
3. System standaryzuje nazwy kolumn w ramce danych zmieniając nazwy na angielskie, sprowadzając wyrazy do małych liter i zastępując spacje znakiem “_”.
4. System analizuje każdą kolumnę w ramce danych pod względem odsetka braków danych.
5. System usuwa z ramki danych wszystkie kolumny o odsetku braków danych większym niż 38%
6. System konwertuje wszystkie zmienne nienumeryczne na zmienne porządkowe o wariantach zdefiniowanych przez programistę metodą ekspercką.
    - Zmienna *rooms* – 4 wariantów.
    - Zmienna *floor* – 7 wariantów.
    - Zmienna *year* – 5 wariantów.
    - Zmienna *landlord_type* – 2 warianty.
    - Zmienna *local_type* – 3 warianty.
    - Zmienna *furnished* – 2 warianty.
    - Zmienna *levels* – 5 wariantów.
7. System tworzy nową ramkę danych, gdzie konwertuje wszystkie zmienne porządkowe na zmienne zerojedynkowe. Każdy wariant staje się nową kolumną o wartości 1 w przypadku kiedy określona obserwacja w poprzedniej ramce danych przyjmowała dany wariant, a wartości 0 jeśli przyjmowała inny wariant. 
8. System przyjmuje zmienną price jako objaśnianą, a zmienne rooms, floor, year, landlord_type, local_type, furnished, levels, area_size jako zmienne objaśniające.
9. System oblicza model regresji liniowej metodą najmniejszych kwadratów.
10. System eksportuje wyliczone parametry modelu do pliku tekstowego params.txt.

### Przebieg działania systemu aplikacji webowej
1. System wczytuje parametry modelu predykcyjnego z pliku params.txt.
2. System generuje stronę internetową z pliku index.html w formie formularza.
3. System akceptuje wartości wprowadzone przez formularz:
    - „*Powierzchnia lokalu*” jako dowolną liczbę całkowitą,
    - „*Liczba pokoi*” jako jeden z elementów listy rozwijanej,
    - „*Piętro*” jako jeden z elementów listy rozwijanej,
    - „*Rocznik budynku*” jako jeden z elementów listy rozwijanej,
    - „*Typ wynajmującego*” jako jeden z elementów listy rozwijanej,
    - „*Przeznaczenie lokalu*” jako jeden z elementów listy rozwijanej,
    - „*Umeblowanie*” jako jeden z elementów listy rozwijanej,
    - „*Liczba kondygnacji*” jako jeden z elementów listy rozwijanej.
4. System konwertuje wprowadzone parametry na listy zerojedynkowe, o kolejności wariantów odpowiadającej kolejności parametrów z listy params.txt, gdzie liczba 1 występuje w miejscu wybranego parametru, a w pozostałych miejscach – 0.
5. System łączy wszystkie listy wariantów w jedna listę ogólną, w kolejności odpowiadającej kolejności zmiennych na liście parametrów params.txt.
6. System dokonuje mnożenia listy wariantów przez listę parametrów.
7. System sumuje wyniki mnożenia z poprzedniego punktu.
8. System generuje podstronę z pliku form.html.
9. System przekazuje wynik mnożenia jako parametr dla podstrony form.html.

## Testy

Poniżej znajdują się scenariusze testów.

### TEST 1

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA  Pozostaw puste pole w oknie “Powierzchnia lokalu”.

c. AKCJA Naciśnij przycisk „Oblicz”.

   OR Wyświetlony jest komunikat błędu

### TEST 2

a. AKCJA Uruchom stronę internetową

   OR Strona załadowała się.

b. AKCJA Wybierz domyślne wartości parametrów.
   
   OR Parametry wybrane pomyślnie.

c. AKCJA Naciśnij przycisk „Oblicz”.
   
   OR Cena wynajmu została obliczona.



### TEST 3

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA Wpisz dowolną wartość liczbową mniejszą niż 5 w polu “Powierzchnia lokalu”, reszta parametrów warianty domyślne.
   
   OR Pozostałe parametry wybrane pomyślnie

c. AKCJA Naciśnij przycisk „Oblicz”.
   
   OR Pojawia się komunikat błędu.


### TEST 4

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA Wpisz wartość 100,3 w polu “Powierzchnia lokalu”.
   
   OR Pojawia się komunikat:
   

c. AKCJA Wpisz liczbę całkowitą w polu “Powierzchnia lokalu”.
   
   OR Wartość zostaje wpisana w okno

d. AKCJA Naciśnij przycisk „Oblicz”.
   
   OR Cena wynajmu została obliczona.


### TEST 5

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA Wpisz wartość nie liczbową w oknie “Powierzchnia lokalu”
   
   OR Pojawia się komunikat:


c. AKCJA Wpisz dowolną wartość liczbową większą lub równą 5 w oknie “Powierzchnia lokalu”
   
   OR Wartość została poprawnie wpisana.


### TEST 6

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA Wpisz wartość “0” w oknie “Powierzchnia lokalu”
   
   OR Pojawia się komunikat:

c. AKCJA Wpisz dowolną wartość liczbową większą lub równą 5 w oknie “Powierzchnia lokalu”
   
   OR Wartość została poprawnie wpisana.



### TEST 7

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA Wpisz wartość “1” w oknie “Powierzchnia lokalu”
   
   OR Pojawia się komunikat:
   

c. AKCJA Wpisz dowolną wartość liczbową większą lub równą 5 w oknie “Powierzchnia lokalu”
   
   OR Wartość została poprawnie wpisana.




### TEST 8

a. AKCJA Uruchom stronę internetową
   
   OR Strona załadowała się.

b. AKCJA Wpisz liczbę ujemną w polu “Powierzchnia lokalu”.
   
   OR Pojawia się komunikat:
   

c. AKCJA Wpisz dowolną wartość liczbową większą lub równą 5 w oknie “Powierzchnia lokalu”
   
   OR Wartość została poprawnie wpisana.


