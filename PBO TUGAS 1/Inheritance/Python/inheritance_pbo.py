# -*- coding: utf-8 -*-
"""Inheritance_PBO

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/135raOtcEdM5OtYOfilhTHardVd6WDRdy
"""

class BangunDatar:
    def Luas(self):
        print("Menghitung Luas Bangun Datar")
    def Keliling(self):
        print("Menghitung Keliling Bangun Datar")

class Persegi(BangunDatar):
    def sisi(self):
        pass

class PersegiPanjang(BangunDatar):
    def panjang(self):
        pass
    def lebar(self):
        pass

class Segitiga(BangunDatar):
    def alas(self):
        pass
    def tinggi(self):
        pass

class Lingkaran(BangunDatar):
    def jari(self):
        pass

class Main(object):
    print("(Bangun Datar)")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    menu = int(input("Pilih Menu : "))

    bangundatar = BangunDatar()
    bangundatar.Luas()
    bangundatar.Keliling()
    
    if menu==1:
        print("\n(Persegi)")
        persegi=Persegi()
        persegi.sisi = int(input("Masukkan Sisi : "))
        persegi.Luas()
        persegi.Keliling()
    elif menu==2:
        print("\n(Persegi Panjang)")
        persegipanjang=PersegiPanjang()
        persegipanjang.panjang = int(input("Masukkan Panjang : "))
        persegipanjang.lebar = int(input("Masukkan Lebar : "))
        persegipanjang.Luas()
        persegipanjang.Keliling()
    elif menu==3:
        print("\n(Segitiga)")
        segitiga=Segitiga()
        segitiga.alas = int(input("Masukkan Alas : "))
        segitiga.tinggi = int(input("Masukkan Tinggi : "))
        segitiga.Luas()
        segitiga.Keliling()
    elif menu==4:
        print("\n(Lingkaran)")
        lingkaran=Lingkaran()
        lingkaran.jari = int(input("Masukkan Jari-Jari : "))
        lingkaran.Luas()
        lingkaran.Keliling()