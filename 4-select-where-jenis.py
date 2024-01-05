import sqlite3
hewan = sqlite3.connect('database_fauna.db')

kursor = hewan.cursor()

kursor.execute("SELECT * FROM FAUNA WHERE jenis = 'mamalia' ")
baris_tabel = kursor.fetchall()

print("DATA HEWAN MAMALIA INDONESIA 2023")
print('='*135)
print("{:<15} {:<25} {:<25} {:<25} {:<25} {:<25}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SEKARANG", "TAHUN DI TEMUKAN"))
print("-"*135)      

for baris in baris_tabel:
    print("{:<15} {:<25} {:<25} {:<25} {:<25} {:<25}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

hewan.close()
