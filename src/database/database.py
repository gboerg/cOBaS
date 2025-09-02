import sqlite3


conn = sqlite3.connect("src/database/cobas.db")
cursor = conn.cursor()