import sqlite3
hewan = sqlite3.connect('database_fauna.db')
kursor = hewan.cursor()

def tampilkan_data_sebelum():
    kursor.execute("SELECT * FROM FAUNA")
    data_sebelum = kursor.fetchall()

    print("DATA FAUNA SEBLUM DI HAPUS")
    for row in data_sebelum:
        print(row)
        
    hewan.close

tampilkan_data_sebelum()

def tampilkan_data_sesudah():
    kursor.execute("DELETE FROM FAUNA WHERE asal = 'kalimantan'")

    kursor.execute("SELECT * FROM FAUNA")
    data_sesudah = kursor.fetchall()

    print("DATA HEWAN SESUDAH DI HAPUS")
    for row in data_sesudah:
        print(row)

    hewan.close()

tampilkan_data_sesudah()