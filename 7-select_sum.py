import sqlite3
hewan = sqlite3.connect('database_fauna.db')
kursor = hewan.cursor()

kursor.execute("SELECT SUM(jml_sekarang) FROM FAUNA")
total_fauna = kursor.fetchone()[0]
print(f"TOTAL POPULASI FAUNA:{total_fauna} ")

hewan.close()