import os

import Class as v

menu = ["[1] Paket Normal"," [2] Login"," [3] exit"]


class Warnet : 
    jls_extract_var = menu

    v.welcome(" Selamat Datang Di Warnet PI","1 jam = 5000          2 jam = 9000         3 jam = 13000",60)
    v.menu(" SILAKAN PILIH MENU ", jls_extract_var, 60)
    #input 1,2,3
    number= eval(input("\nMasukkan pilihan :"))
    if number == 1 :
        print("1 jam = 5000          2 jam = 9000         3 jam = 13000")
        pilihan=eval(input("\nPilihan paket :"))
        if pilihan==1:
            v.pembayaran(pilihan)
        elif pilihan==2:
            v.pembayaran(pilihan)
        elif pilihan==3:
            v.pembayaran(pilihan)
    if number == 2:
        v.headerlogin(60)
