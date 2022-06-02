import matplotlib.pyplot as plt
import numpy as np
import penskalaan as ps
import refleksi as rs
import rotasi as rt
import translasi as ts
import sys

print("===============================")
print("Menu Transformasi-Geometri :")
print("===============================")

print("===============================")
print("1. Penskalaan   ")
print("===============================")
print("2. Refleksi  ")
print("===============================")
print("3. Rotasi")
print("===============================")
print("4. Translasi")
print("===============================")
print("5. Keluar")
print("===============================")

PIL = int(input("Masukan Pilihan Anda: "))

if PIL == 1:

    ps.show()

elif PIL == 2:
    rs.show()

elif PIL == 3:
    rt.show()

elif PIL == 4:
    ts.show()
else:

    print("Maaf, Anda Salah Memasukan Angka")
    print("Silahkan Coba Lagi")
    sys.exit()
