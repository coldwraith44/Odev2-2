import pyodbc



db= pyodbc.connect('Driver={SQL Server};'
                      'Server=AUT;'
                      'Database=liman_veri_tabani;'
                      'Trusted_Connection=yes;')
cursor=db.cursor()



i1="gemi_tablo"

sql_q=(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i1}'")
cursor.execute(sql_q)

k1=cursor.fetchone()

if k1[0]==1:

    pass

else:
     cursor.execute(f'''
    CREATE TABLE {i1}  (
    seri_no VARCHAR(255) PRIMARY KEY,
    adi VARCHAR(250) NOT NULL,
    agirlik DECIMAL(10, 2)  NOT NULL,
    yapim_yili DATE NOT NULL
    )
    ''')



i2="yolcu_gemisi_tablo"

sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i2}'"
cursor.execute(sql_q)

k2=cursor.fetchone()

if k2[0]==1:

    pass

else:

    cursor.execute(f'''
    CREATE TABLE {i2} (
        seri_no VARCHAR(255) PRIMARY KEY,
        yolcu_kapasitesi INT NOT NULL,
        FOREIGN KEY (seri_no) REFERENCES gemi_tablo(seri_no)
    )
    ''')
i3="petrol_tankeri_tablo"

sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i3}'"
cursor.execute(sql_q)

k3=cursor.fetchone()

if k3[0]==1:

    pass

else:

    cursor.execute(f'''
    CREATE TABLE {i3} (
    seri_no VARCHAR(255) PRIMARY KEY,
    petrol_kapasitesi DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (seri_no) REFERENCES gemi_tablo(seri_no)
    )
    ''')

i4="konteyner_gemi_tablo"

sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i4}'"
cursor.execute(sql_q)

k4=cursor.fetchone()

if k4[0]==1:

    pass
else:

    cursor.execute(f'''
    CREATE TABLE {i4}(
    seri_no VARCHAR(255) PRIMARY KEY,
    konteyner_sayisi INT NOT NULL,
    maks_agirlik DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (seri_no) REFERENCES gemi_tablo(seri_no)
    )
    ''')

i7="kaptanlar_tablo"
sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i7}'"
cursor.execute(sql_q)

k7=cursor.fetchone()

if k7[0]==1:

    pass
else:
   cursor.execute(f'''
    CREATE TABLE {i7} (
    kaptan_no VARCHAR(255) PRIMARY KEY,
    ad VARCHAR(255) NOT NULL,
    soyad VARCHAR(255) NOT NULL,
    adres VARCHAR(255) NOT NULL,
    vatandaslik VARCHAR(50) NOT NULL,
    dogum_tarihi DATE NOT NULL,
    ise_giris_tarihi DATE NOT NULL,
    lisans VARCHAR(255) NOT NULL
    )
    ''')

i8="murettebat_tablo"
sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i8}'"
cursor.execute(sql_q)

k8=cursor.fetchone()

if k8[0]==1:

    pass
else:
   cursor.execute(f'''
    CREATE TABLE {i8}(
    murettebat_no VARCHAR(255) PRIMARY KEY,
    ad VARCHAR(255) NOT NULL,
    soyad VARCHAR(255) NOT NULL,
    adres VARCHAR(255),
    vatandaslik VARCHAR(50) NOT NULL,
    dogum_tarihi DATE NOT NULL,
    ise_giris_tarihi DATE NOT NULL,
    gorev VARCHAR(255) NOT NULL
    )
    ''')





i5="seferler_tablo"
sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i5}'"
cursor.execute(sql_q)

k5=cursor.fetchone()

if k5[0]==1:

    pass
else:
   cursor.execute(f'''
        CREATE TABLE {i5} (
        sefer_no VARCHAR(255) PRIMARY KEY,
        gemi_no VARCHAR(255) NOT NULL,
        kaptanlar VARCHAR(255) NOT NULL,
        murettebat VARCHAR(255) NOT NULL,
        yola_cikis_tarihi DATE NOT NULL,
        donus_tarihi DATE NOT NULL,
        yola_cikis_limani VARCHAR(255) NOT NULL,
        ugranilan_limanlar VARCHAR(255) NULL,
        FOREIGN KEY (gemi_no) REFERENCES gemi_tablo(seri_no),
        FOREIGN KEY (kaptanlar) REFERENCES kaptanlar_tablo(kaptan_no),
        FOREIGN KEY (murettebat) REFERENCES murettebat_tablo(murettebat_no)
        )
        ''')

i6="limanlar_tablo"
sql_q=f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{i6}'"
cursor.execute(sql_q)

k6=cursor.fetchone()



if k6[0]==1:

    pass
else:
    cursor.execute(f'''
    CREATE TABLE {i6} (
    liman_adi VARCHAR(255) NOT NULL,
    ulke VARCHAR(255) NOT NULL,
    limandaki_gemiler VARCHAR(255) NULL,
    nufus INT NOT NULL,
    pasaport_istiyor_mu BIT NOT NULL,
    demirleme_ucreti DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (liman_adi, ulke),
    FOREIGN KEY (limandaki_gemiler) REFERENCES gemi_tablo(seri_no)
    )
    ''')
db.commit()






"""# Kaptanlar tablosuna gerçekçi veri ekle
kaptan_verileri = [
    ('Kaptan1', 'Ahmet', 'Yılmaz', 'İstanbul', 'Türk', '1975-01-15', '2000-05-20', 'Kaptanlık Lisansı A'),
    ('Kaptan2', 'Mehmet', 'Kaya', 'Ankara', 'Türk', '1980-03-22', '2005-08-10', 'Kaptanlık Lisansı B'),
    ('Kaptan3', 'Ayşe', 'Demir', 'İzmir', 'Türk', '1978-07-10', '2010-02-18', 'Kaptanlık Lisansı C'),
    ('Kaptan4', 'Fatma', 'Şahin', 'Bursa', 'Türk', '1985-05-30', '2015-04-05', 'Kaptanlık Lisansı D'),
    ('Kaptan5', 'Mustafa', 'Yıldız', 'Antalya', 'Türk', '1990-09-12', '2020-10-15', 'Kaptanlık Lisansı E')
]

for kaptan in kaptan_verileri:
    cursor.execute(f"INSERT INTO kaptanlar_tablo (kaptan_no, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, lisans) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   kaptan)

# Mürettebat tablosuna gerçekçi veri ekle
murettebat_verileri = [
    ('Mürtebat1', 'Ahmet', 'Kaya', 'İstanbul', 'Türk', '1978-02-20', '2001-06-15', 'Güverte Görevlisi'),
    ('Mürtebat2', 'Ayşe', 'Demir', 'Ankara', 'Türk', '1982-06-10', '2006-09-22', 'Makine Görevlisi'),
    ('Mürtebat3', 'Mehmet', 'Şahin', 'İzmir', 'Türk', '1985-08-15', '2010-11-18', 'Yemek Görevlisi'),
    ('Mürtebat4', 'Fatma', 'Yıldız', 'Bursa', 'Türk', '1990-04-25', '2015-12-05', 'Temizlik Görevlisi'),
    ('Mürtebat5', 'Mustafa', 'Yılmaz', 'Antalya', 'Türk', '1995-11-30', '2021-03-10', 'Güvenlik Görevlisi')
]

for murettebat in murettebat_verileri:
    cursor.execute(f"INSERT INTO murettebat_tablo (murettebat_no, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, gorev) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   murettebat)"""
import random
from datetime import datetime, timedelta





gemiler = ['Gemi1', 'Gemi2', 'Gemi3', 'Gemi4', 'Gemi5', 'Gemi6', 'Gemi7', 'Gemi8', 'Gemi9']
gemiler1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
tarihler=[]
for _ in range(9):
    start_date = datetime.now() - timedelta(days=random.randint(1, 365))
    end_date = datetime.now() + timedelta(days=random.randint(1, 365))
    random_date = start_date + (end_date - start_date) * random.random()
    tarihler.append(random_date)

for i in range(9):
    cursor.execute(f"INSERT INTO gemi_tablo (seri_no, adi, agirlik,yapim_yili) VALUES (?, ?, ?, ?)",
                   (gemiler[i], gemiler1[i], random.uniform(1000, 5000), tarihler[i]))


for i in range(3):
    cursor.execute(f"INSERT INTO konteyner_gemi_tablo (seri_no, konteyner_sayisi, maks_agirlik) VALUES (?, ?, ?)",
                   (gemiler[i], random.randint(100, 1000), random.uniform(1000, 5000)))


for i in range(3):
    cursor.execute(f"INSERT INTO yolcu_gemisi_tablo (seri_no, yolcu_kapasitesi) VALUES (?, ?)",
                   (gemiler[i], random.randint(100, 500)))


for i in range(3):
    cursor.execute(f"INSERT INTO petrol_tankeri_tablo (seri_no, petrol_kapasitesi) VALUES (?, ?)",

                                    (gemiler[i], random.uniform(1000, 10000)))

for i in range(5):
    cursor.execute(f"INSERT INTO limanlar_tablo (liman_adi, ulke, limandaki_gemiler, nufus, pasaport_istiyor_mu, demirleme_ucreti) VALUES (?, ?, ?,  ?, ?, ?)",
                   (f'Liman{i+1}', 'Ülke',gemiler[i] ,random.randint(10000, 1000000), random.choice([0, 1]), random.uniform(1000, 10000)))


for i in range(4):
    cursor.execute(f"INSERT INTO seferler_tablo (sefer_no, gemi_no, kaptanlar, murettebat, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani, ugranilan_limanlar) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (f'Sefer{i+1}', random.choice(gemiler), f'Kaptan{i+1}', f'Mürtebat{i+1}', datetime.now(), datetime.now() + timedelta(days=random.randint(1, 30)), 'Yola Çıkış Limanı', 'Uğranılan Limanlar'))


tablo_adi = 'kaptanlar_tablo'


primary_key_sutun = 'kaptan_no'


sql_sorgusu = f"SELECT {primary_key_sutun} FROM {tablo_adi}"


cursor.execute(sql_sorgusu)


print("Primary Key'ler:")
for row in cursor.fetchall():
    print(row[0])



aranan_deger = 'Kaptan6'


sql_sorgusu = "SELECT * FROM kaptanlar_tablo WHERE kaptan_no = ?"


cursor.execute(sql_sorgusu, (aranan_deger,))


row = cursor.fetchone()
if row:
    print(f"'{aranan_deger}' değeri tabloda bulunuyor.")
else:
    print(f"'{aranan_deger}' değeri tabloda bulunmuyor.")
db.commit()

silinecek_deger = 'Kaptan5'


sql_sorgusu = "DELETE FROM kaptanlar_tablo WHERE kaptan_no = ?"


cursor.execute(sql_sorgusu, (silinecek_deger,))


db.commit()



aranan_deger = 'Kaptan1'


sql_sorgusu = "SELECT * FROM kaptanlar_tablo WHERE kaptan_no = ?"


cursor.execute(sql_sorgusu, (aranan_deger,))

row = cursor.fetchone()
if row:
    print("Bulunan Satır:", row)
else:
    print(f"'{aranan_deger}' değeri tabloda bulunmuyor.")

yeni_isim = 'Mehmet'
aranan_deger = 'Kaptan1'


sql_sorgusu = "UPDATE kaptanlar_tablo SET ad = ? WHERE kaptan_no = ?"


cursor.execute(sql_sorgusu, (yeni_isim, aranan_deger))

db.commit()

cursor.close()
db.close()
