import sqlite3

# Úkol 1: Návrh databáze a záznam mapy ze vzorového orientovaného grafu
def create_and_populate_database():
    # Připojení k databázi (vytvoření nové pokud neexistuje)
    conn = sqlite3.connect('mapa.db')
    cursor = conn.cursor()

    # Vytvoření tabulek
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Nodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Edges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_node_id INTEGER,
        end_node_id INTEGER,
        distance REAL,
        is_bidirectional BOOLEAN,
        FOREIGN KEY (start_node_id) REFERENCES Nodes(id),
        FOREIGN KEY (end_node_id) REFERENCES Nodes(id)
    )
    ''')

    # Vložení uzlů
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for node in nodes:
        cursor.execute('INSERT INTO Nodes (name) VALUES (?)', (node,))

    # Vložení cest
    edges = [
        ('A', 'B', 1.0, True),
        ('B', 'D', 2.0, False),
        ('C', 'F', 3.0, False),
        ('D', 'E', 1.0, True),
        ('F', 'G', 1.5, False),
        ('H', 'I', 2.5, False)
    ]

    for start, end, distance, is_bidirectional in edges:
        cursor.execute('''
        INSERT INTO Edges (start_node_id, end_node_id, distance, is_bidirectional) 
        VALUES (
            (SELECT id FROM Nodes WHERE name=?), 
            (SELECT id FROM Nodes WHERE name=?), 
            ?, 
            ?
        )''', (start, end, distance, is_bidirectional))

    # Uložení změn a uzavření připojení
    conn.commit()
    conn.close()

# Úkol 2: Návrh datové struktury pro záznam údajů z mapy
def initialize_data_structure():
    return {}

# Úkol 3: Načtení mapy z databáze do datové struktury
def load_map_from_database():
    # Připojení k databázi
    conn = sqlite3.connect('mapa.db')
    cursor = conn.cursor()

    # Načtení uzlů
    nodes = {}
    cursor.execute("SELECT id, name FROM Nodes")
    for node_id, name in cursor.fetchall():
        nodes[name] = {}

    # Načtení cest
    cursor.execute("SELECT start_node_id, end_node_id, distance, is_bidirectional FROM Edges")
    for start_node_id, end_node_id, distance, is_bidirectional in cursor.fetchall():
        # Získání jmen uzlů podle jejich id
        cursor.execute("SELECT name FROM Nodes WHERE id=?", (start_node_id,))
        start_node = cursor.fetchone()[0]
        cursor.execute("SELECT name FROM Nodes WHERE id=?", (end_node_id,))
        end_node = cursor.fetchone()[0]

        # Přidání cesty do datové struktury
        nodes[start_node][end_node] = distance
        if is_bidirectional:
            nodes[end_node][start_node] = distance

    # Uzavření připojení k databázi
    conn.close()
    
    return nodes

# Úkol 4: Zobrazení načtené mapy na výstupu
def display_map(nodes):
    for node, connections in nodes.items():
        print(f"Node {node}:")
        for connected_node, distance in connections.items():
            print(f"  - Connects to {connected_node} with distance {distance}")

# Hlavní funkce, která vykonává všechny úkoly
def main():
    # Úkol 1: Vytvoření a naplnění databáze
    create_and_populate_database()

    # Úkol 2: Inicializace datové struktury
    nodes = initialize_data_structure()

    # Úkol 3: Načtení mapy z databáze do datové struktury
    nodes = load_map_from_database()

    # Úkol 4: Zobrazení načtené mapy na výstupu
    display_map(nodes)

# Spuštění hlavní funkce
if __name__ == "__main__":
    main()
