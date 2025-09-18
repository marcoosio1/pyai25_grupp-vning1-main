# Student APP Pymasters

Uppdelning av uppgifter:
- Marcus Main
- Pontus Student
- Osman Event
- Sergey Todo

## Intro
Det här repo:t är tänkt att agera som ett skelett för ett grupparbet i kursen Grundläggande programmering i Python. Antal tilltänkta gruppmedlemmar är max 4 men går bra med färre. 

Tanken är att varje gruppmedlem väljer någon av filerna att arbeta med, main.py, student.py, todo.py, event.py, och skriver kod för varje skapad funktion i den filen.

### main.py
I den här filen ska själva huvudprogrammet ligga. Möjligheten att utföra alla tänkbara saker så som att:
- Skapa studenter
- Lägga till kurser
- Skapa events
- Lägga till studenter på event
- Skapa todos
- etc etc

### student.py
I den här filen ska all logik för hur studenter skapas och hanteras ligga. Viktigt är att information inte ska läcka ut. Vi vill att det ska stanna i filen.

### event.py
I den här filen ska all logik för hur events skapas och hanteras ligga. Viktigt är att information inte ska läcka ut. Vi vill att det ska stanna i filen.

### todo.py
I den här filen ska all logik för hur todos skapas och hanteras ligga. Viktigt är att information inte ska läcka ut. Vi vill att det ska stanna i filen.

---

## Funktioner
De tilltänkta filerna är stängda för förändring i den mån att ni inte får ta bort funktioner eller döpa om dem. Det är dock tillåtet att utöka med fler funktioner och funktionalitet om så önskas! Kom ihåg att hålla koll på signaturen för varje funktion, vad de har för parameter-typer och retur-typer.

### Ansvar
Kom ihåg att varje gruppmedlem ansvara för sin egna fil att det ska fungera. Tanken med den här uppgiften är att ni ska kunna sammarbeta utan att göra varandras arbete. Ni får dock gärna diskutera och ge tips till varandra men jag vill inte att ni kopierar från varandra eller som tidigare sagt, gör någons annans arbete. 

### Arbetsflöde
Tänk igenom arbetsflödet

#### Branches
Skapa vettiga branches, tex en för varje implementering av någon funktion eller en master-sidebranch som innehåller i sig egna branches för varje funktion osv.

#### Testa funktioner
I varje fil finns det en kodsnutt:
```python
if __name__ == "__main__":
    ...
```
Den här kodsnutten gör att all kod ni lägger indenterat under if-satsen kommer bara köras om ni kör den specifika filen! Här kan ni skriva små tester på funktionerna ni skapar för att säkerställa att de gör vad ni förväntar er. 

