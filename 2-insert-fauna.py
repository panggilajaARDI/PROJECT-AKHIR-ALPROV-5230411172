import sqlite3
hewan = sqlite3.connect('database_fauna.db')

hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('harimau jawa', 'mamalia', 'jawa', '40', '2019' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('kuskus beruang', 'mamalia', 'sulawesi', '30', '2021' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('beruang madu', 'mamalia', 'sumatra', '1000', '2020' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('pesut mahakam', 'mamalia', 'kalimantan', '100', '2021' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('burung maleo', 'burung', 'sulawsi', '7000', '2023' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('macan dahan', 'mamalia', 'sumatra', '400', '2020' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('kancil', 'mamalia', 'jawa', '60', '2022' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('gajah kalimantan', 'mamalia', 'kalimantan', '1500', '2021' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('elang jawa', 'burung', 'jawa', '200', '2021' )
                ''')
hewan.execute(f'''
                INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_sekarang, thn_ditemukan)
                VALUES('katak borneo', 'amfibi', 'kalimantan', '2000', '2023' )
                ''')
hewan.commit()
hewan.close()
