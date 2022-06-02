# Program Transformasi Geometri

Simulasi untuk transformasi geometri 2 dimensi dengan menggunakan Antarmuka Pemrograman Aplikasi Matplotlib

## Memulai

Buka folder transformasi-geo-2d lalu ketuk run pada file yang ingin dijalankan :
seperti file utama terletak pada
main.py

```
atau bisa mencoba menjalankan satu persatu file
penskalaan.py, refleksi.py, rotasi.py, translasi.py
```

_starting-up pada program agak lambat_
Lalu program akan menampilkan 2 buah jendela program.
Yang 1 adalah terminal dan 1 lagi adalah jendela untuk tampilan grafik.
Pada jendela terminal akan tertulis :

```
--------------SELAMAT DATANG----------------
---------Menu Transformasi-Geometri---------

Masukan titik-titik koordinat Segitiga :
```

### Pustaka yang digunakan

```
pyOpenGL
numpy
math
matplotlib
sys
```

## Menggunakan Program

Berikut ini adalah cara menggunakan program :

### Memasukkan Titik Sudut

Contoh masukan :
1/2/3/4 bisa memilih antara 1-4

```
('Masukan titik untuk nilai A x:'))
('Masukan titik untuk nilai A y:'))
('Masukan titik untuk nilai B x:'))
('Masukan titik untuk nilai B y:'))
('Masukan titik untuk nilai C x:'))
('Masukan titik untuk nilai C y:'))
```

# ---------------------Masukan titik skala-----------------------

Masukan titik skala x:1
Masukan titik skala y:2
=================================================================

### Perintah

Daftar perintah-perintah dasar:
Translasi objek searah x sejauh dx dan searah y sejauh dy.

```
translate dx dy
```

Dilatasi objek k kali.

```
dilate k
```

Rotasi objek deg derajat dengan poros (a,b).

```
rotate deg a b
```

Refleksi objek berdasarkan parameter <x, y, y=x, y=-x>.

```
reflect parameter
```

Menggusur objek searah param <x atau y> dengan faktor k.

```
shear param k
```

Meregangkan objek searah param <x atau y> dengan faktor k.

```
stretch param k
```

Transformasi objek dengan matrix bebas
a c
b d

```
custom a b c d
```

Melakukan transformasi sekaligus sebanyak n kali.

```
multiple n
command parameter
command parameter
.
.
.
```

Mengembalikan objek ke posisi awal.

```
reset
```

Keluar program.

```
exit
```

### Contoh penggunaan program :

```



===============================================================
-------------------------SELAMAT DATANG------------------------
-----------Masukan titik-titik koordinat Segitiga--------------
===============================================================
Masukan titik untuk nilai A x:2
Masukan titik untuk nilai A y:4
Masukan titik untuk nilai B x:2
Masukan titik untuk nilai B y:4
Masukan titik untuk nilai C x:3
Masukan titik untuk nilai C y:6
===============================================================
---------------------Masukan titik skala-----------------------
===============================================================
Masukan titik skala x:1
Masukan titik skala y:2
===============================================================
-----------------------Hasil Skala-----------------------------
===============================================================
A' [2, 8]
B' [2, 8]
C' [3, 12]
=========================================================
    MASUKAN PILIHAN REFLEKSI
=========================================================
     1. REFLEKSI sumbu x : P(x,y) -> P'(x,-y)
     2. REFLEKSI sumbu y : P(x,y) -> P'(-x,y)
     3. REFLEKSI sumbu y = x : P(x,y) -> P'(y,x)
     4. REFLEKSI titik 0 : P(x,y) -> P'(-x,-y)
     5. REFLEKSI sumbu x = h : P(x,y) -> P'(2h - x,y)
     6. REFLEKSI sumbu y = h : P(x,y) -> P'(x,2h - y)
     7. REFLEKSI sumbu y = -x : P(x,y) -> P'(-y,-x)
=========================================================
Masukan Pilihan Anda: 6
=========================================================
=====  6. ANDA memilih REFLEKSI sumbu y = h : P(x,y) -> P'(x,2h - y)
=========================================================
Masukan titik y: 1
=========================================================
Masukan titik untuk nilai A x:2
Masukan titik untuk nilai A y:1
Masukan titik untuk nilai B x:2
Masukan titik untuk nilai B y:1
Masukan titik untuk nilai C x:1
Masukan titik untuk nilai C y:1
=========================================================
=   Hasil REFLEKSI TERHADAP sumbu y = h : P(x,y) -> P'(x,2h - y)
=========================================================
A' [2, 1]
B' [2, 1]
C' [1, 1]
===============================================================
```
