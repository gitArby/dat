### README

# Projekt: Mapa Orientovaného Grafu

Tento projekt slouží k vytvoření, naplnění, načtení a zobrazení mapy orientovaného grafu pomocí SQLite databáze a Pythonu. Projekt je rozdělen do několika kroků, které jsou vysvětleny níže.

## Požadavky

1. **Python**: Kód je napsán v Pythonu, proto je potřeba mít nainstalovaný Python na vašem počítači. Doporučená verze je Python 3.6 nebo novější.
2. **SQLite**: K práci s databází používáme SQLite, který je součástí standardní knihovny Pythonu.

## Instalace

1. **Nainstalujte Python**:
   - Stáhněte a nainstalujte Python z [oficiálních stránek](https://www.python.org/downloads/).

2. **Stažení projektu**:
   - Stáhněte tento projekt z GitHubu nebo jiného zdroje jako ZIP soubor a rozbalte ho do složky na vašem počítači.

## Struktura projektu

Projekt obsahuje následující soubory:

- `mapa.db`: SQLite databáze, která bude vytvořena a naplněna kódem.
- `main.py`: Hlavní Python skript, který provádí všechny úkoly (vytvoření databáze, naplnění daty, načtení dat a zobrazení mapy).

## Spuštění projektu

Postupujte podle následujících kroků pro spuštění projektu:

1. **Otevřete terminál**:
   - Na Windows: Otevřete příkazový řádek nebo PowerShell.
   - Na Mac nebo Linux: Otevřete terminál.

2. **Navigujte do složky s projektem**:
   - Pomocí příkazu `cd` přejděte do složky, kde jste rozbalili projekt. Například:
     ```
     cd C:\cesta\k\projektu
     ```

3. **Spusťte Python skript**:
   - Zadejte následující příkaz pro spuštění hlavního skriptu:
     ```
     python main.py
     ```

4. **Výsledek**:
   - Skript vytvoří databázi `mapa.db`, naplní ji daty, načte data do datové struktury a zobrazí mapu na výstupu (v terminálu). Výstup by měl vypadat nějak takto:
     ```
     Node A:
       - Connects to B with distance 1.0
     Node B:
       - Connects to D with distance 2.0
     Node D:
       - Connects to E with distance 1.0
     Node E:
       - Connects to D with distance 1.0
     Node C:
       - Connects to F with distance 3.0
     Node F:
       - Connects to G with distance 1.5
     Node G:
     Node H:
       - Connects to I with distance 2.5
     Node I:
     ```

## Popis kódu

### Hlavní skript (`main.py`)

Skript je rozdělen do čtyř hlavních funkcí:

1. **create_and_populate_database()**:
   - Vytvoří databázi, tabulky a naplní je daty ze vzorového orientovaného grafu.

2. **initialize_data_structure()**:
   - Inicializuje datovou strukturu (prázdný slovník) pro mapu.

3. **load_map_from_database()**:
   - Načte data z databáze a uloží je do datové struktury.

4. **display_map(nodes)**:
   - Zobrazí načtenou mapu na výstupu v terminálu.

### Hlavní funkce (`main()`)

- Hlavní funkce postupně vykoná všechny kroky (vytvoření a naplnění databáze, inicializace datové struktury, načtení dat a zobrazení mapy).

## Závěr

Tento projekt ukazuje základní práci s databázemi v Pythonu a způsob, jakým lze data z databáze načítat a zobrazovat. Pokud budete mít jakékoli dotazy nebo problémy, neváhejte se obrátit na svého učitele nebo konzultovat dokumentaci k Pythonu a SQLite.
