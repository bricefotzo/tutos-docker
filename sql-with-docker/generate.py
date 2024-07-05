import sqlite3

# Créer une nouvelle base de données SQLite
conn = sqlite3.connect('example.db')

# Créer une table
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, date TEXT, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))''')

# Insérer des données
c.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@email.com')")
c.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@email.com')")
c.execute("INSERT INTO orders (date, user_id) VALUES ('2021-10-10', 1)")
c.execute("INSERT INTO orders (date, user_id) VALUES ('2021-10-11', 1)")
c.execute("INSERT INTO orders (date, user_id) VALUES ('2021-10-12', 2)")

# Sauvegarder les changements
conn.commit()

# Fermer la connexion
conn.close()
