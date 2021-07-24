CREATE DATABASE sirket;
USE sirket;

CREATE TABLE birim (
birim_no INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
birim_ad VARCHAR(20) UNIQUE NOT NULL
);

INSERT INTO birim VALUES ('KALİTE'),('İDARİ'),('ARGE'),('TEKNİK');

CREATE TABLE unvan (
unvan_no INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
unvan_ad VARCHAR(20) UNIQUE NOT NULL
);

INSERT INTO unvan VALUES ('MÜHENDİS'),('İK UZMANI'),('TEKNİSYEN');

CREATE TABLE il (
il_no CHAR(2) PRIMARY KEY,
il_ad VARCHAR(20) UNIQUE NOT NULL
);

INSERT INTO il(il_no, il_ad) VALUES ('06','ANKARA'),('34','İSTANBUL'),('35','İZMİR');

CREATE TABLE ilce (
ilce_no INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
ilce_ad VARCHAR(20) NOT NULL,
il_no CHAR(2) NOT NULL REFERENCES il(il_no),
CONSTRAINT ilceTekil UNIQUE (ilce_ad,il_no)
);

INSERT INTO ilce(ilce_ad, il_no) VALUES 
('ÇANKAYA','06'),('POLATLI','06'),('YENİMAHALLE','06'),('AVCILAR','34'),
('BEYLİKDÜZÜ','34'),('ESENYURT','34'),('BUCA','35'),('KARŞIYAKA','35'),('KONAK','35');

CREATE TABLE proje (
proje_no INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
proje_ad VARCHAR(20) UNIQUE NOT NULL,
baslama_tarihi DATE NOT NULL,
planlanan_bitis_tarihi DATE NOT NULL
);

INSERT INTO proje(proje_ad, baslama_tarihi, planlanan_bitis_tarihi) VALUES
('TEMİZ DÜNYA','2015.01.20','2017.01.11'),
('GÜVENLİ INTERNET','2017.05.15','2020.06.09'),
('MUTLU ŞEHİR','2017.07.11','2019.11.29'),
('AKILLI EVLER','2018.02.10','2021.11.29'),
('SESSİZ ORTAM','2018.03.01','2019.11.29');