import os
from re import T
from tkinter import BROWSE

import Class as v

menu = ["[1] Paket Normal"," [2] Login"," [3] exit"]


class Warnet : 
    jls_extract_var = menu

    while True:
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
        elif number == 2:
            v.login(60)
        elif number == 3:
            v.exit(60)
            break;
        exit=eval(input("\nKlik 1 untuk melanjutkan :"))
        if exit!=1:
            v.exit(60)
            break
    
