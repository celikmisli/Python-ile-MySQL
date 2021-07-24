#Veri Tabanı Oluşturma

import mysql.connector

mislidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlkullanıyorum123"
)

mycursor=mislidb.cursor()

mycursor.execute("CREATE DATABASE sirket")

# Tüm Veri Tabanlarını Görüntüleme

import mysql.connector

mislidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlkullanıyorum123"
)

mycursor=mislidb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor: #For komutu kullanma sebebimiz tüm verileri bizlere sunabilmesidir.  Yani kayıtların hepsi gelene kadar devam etmesi gerekir.
    print(x)

#Belirli bir veritabanına bağlantı gerçekleştirmek

import mysql.connector

mislidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlkullanıyorum123",
    database="sirket"
)

mycursor=mislidb.cursor()

#Tablo Oluşturma

import mysql.connector

mislidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlkullanıyorum123",
    database="sirket"
)

mycursor=mislidb.cursor()

mycursor.execute(
    "CREATE TABLE proje (proje_no INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, proje_ad VARCHAR(20) UNIQUE NOT NULL,baslama_tarihi DATE NOT NULL,planlanan_bitis_tarihi DATE NOT NULL)"
 )

# İnsert ile tabloya veri ekleme

import mysql.connector

def KayitEkle(): #fonksiyon komutu ile yapmamızın sebebi bir değer atayacak olmamız ve bu değeri gönderecek olmamızdır
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()

    sql="INSERT INTO proje(proje_ad, baslama_tarihi, planlanan_bitis_tarihi) VALUES(%s, %s, %s)"
    values=("TEMİZ DÜNYA","2015.01.20","2017.01.11")

    cursor.execute(sql, values)

    try:
        giris.commit() #commit etmek demek verileri kalıcı olarak veri tabanına eklemek demektir. 
    #Try except bloğuna yerleştirmemizin sebebi bu işlemi gerçekleştirebildiğimizi görebilmektir.
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        giris.close
        print("Bağlantı ve ekleme işlemi sağlandı")


KayitEkle()

# İnsert ile Tabloya bir çok veri ekleme

import mysql.connector

def KayitEkle(proje_ad, baslama_tarihi, planlanan_bitis_tarihi):
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()

    sql="INSERT INTO proje(proje_ad, baslama_tarihi, planlanan_bitis_tarihi) VALUES(%s, %s, %s)"
    values=(proje_ad, baslama_tarihi, planlanan_bitis_tarihi)
    cursor.execute(sql, values)

    try:
        giris.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        giris.close
        print("Bağlantı ve ekleme işlemi sağlandı")

while True:
    proje_ad=str(input("Proje adı giriniz: "))
    baslama_tarihi=input("Başlama tarihi giriniz: ")
    planlanan_bitis_tarihi=input("Planlanan bitiş tarihini giriniz: ")



    msg=("Devam etmek istiyor musunuz? (e/h)")
    if msg =="h":
        print("Kayıtlarınız veri tabanına eklendi")

    KayitEkle(proje_ad, baslama_tarihi, planlanan_bitis_tarihi)


#SELECT sorgusu kullanımı

import mysql.connector

def KayitEkle():
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()
    cursor.execute("SELECT * FROM birim")

    kayit=cursor.fetchall() #birden fazla kayıt görüntülemek istediğimizde kullanırız...

    print(kayit)
        
KayitEkle()

#WHERE Komutu Kullanımı

import mysql.connector

def KayitEkle():
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()
    cursor.execute("SELECT * FROM birim WHERE birim_ad='KALİTE'")

    kayit=cursor.fetchall() #birden fazla kayıt görüntülemek istediğimizde kullanırız...

    print(kayit)
    
KayitEkle()

# ORDER BY Kullanımı

import mysql.connector

def KayitEkle():
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()
    cursor.execute("SELECT * FROM birim ORDER BY birim_no")

    kayit=cursor.fetchall() #birden fazla kayıt görüntülemek istediğimizde kullanırız...

    print(kayit)

KayitEkle()

#UPDATE Komutu

import mysql.connector

def KayitEkle():
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()

    SQL=("UPDATE ilce SET ilce_ad='YENİMAHALLE' WHERE ilce_no=9")

    cursor.execute(SQL)

    try:
        giris.commit() 
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        giris.close
        print("Bağlantı ve güncelleme işlemi sağlandı")
KayitEkle()

#Join İşlemi

import mysql.connector

def KayitEkle():
    giris=mysql.connector.connect(host="localhost",user="root",password="mysqlkullanıyorum123",database="sirket")
    cursor=giris.cursor()

    SQL=("SELECT il.il_ad, ilce.ilce_ad FROM il inner join ilce ON il.il_no=ilce.il_no")

    cursor.execute(SQL)

    try:
        kayit=cursor.fetchall()
        for i in kayit:
            print(i)
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        giris.close
        print("Bağlantı ve join işlemi sağlandı")

KayitEkle()



