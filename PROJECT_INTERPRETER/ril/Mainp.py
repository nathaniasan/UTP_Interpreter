import os
from re import T
from tkinter import BROWSE
import time

import Class as v

menu = ["[1] Paket Normal"," [2] Login"," [3] exit"]
menu1 = ["[1] Paket untuk Member"," [2] Login"," [3] exit"]

class Warnet : 
    jls_extract_var = menu
    menumember = menu1

    while True:
        v.welcome(" Selamat Datang Di Warnet PI","1 jam = 5000          2 jam = 9000         3 jam = 13000",60)
        v.menu(" SILAKAN PILIH MENU ", jls_extract_var, 60)
        #input 1,2,3
        while True:
            try:
                number= eval(input("\nMasukkan pilihan :"))
            except (SyntaxError,NameError):
                print("pilihan invalid")
                continue
            break
        if number == 1 :
            print("1 jam = 5000          2 jam = 9000         3 jam = 13000") 
            while True:
                try:
                    pilihan=eval(input("\nPilihan paket :"))
                except (SyntaxError,NameError):
                    print("pilihan invalid")
                    continue
                break
            
            if pilihan==1:
                v.pembayaran(pilihan)
                print ('Waktu penggunaan berakhir pada pukul ', v.struct(pilihan))
                
            elif pilihan==2:
                v.pembayaran(pilihan)
                print ('Waktu penggunaan berakhir pada pukul ', v.struct(pilihan))

            elif pilihan==3:
                v.pembayaran(pilihan)
                print ('Waktu penggunaan berakhir pada pukul ', v.struct(pilihan))

            else:
                print("\nPilihan invalid......!\n")
                continue
        elif number == 2:
            v.login(60)
            v.menu(" SILAKAN PILIH PAKET SEBAGAI MEMBER",menumember, 60)
            while True:
                try:
                    number= eval(input("\nMasukkan pilihan :"))
                except (SyntaxError,NameError):
                    print("pilihan invalid")
                    continue
                break
            if number == 1 :
                print("1 jam = 4000          2 jam = 7000         3 jam = 10000") 
                while True:
                    try:
                        p=eval(input("\nPilihan paket :"))
                    except (SyntaxError,NameError):
                        print("pilihan invalid")
                        continue
                    break
                if p==1:
                    v.pembayaranMember(p)
                    print ('Waktu penggunaan berakhir pada pukul ', v.struct(pilihan))
                elif p==2:
                    v.pembayaranMember(p)
                    print ('Waktu penggunaan berakhir pada pukul ', v.struct(pilihan))
                elif p==3:
                    v.pembayaranMember(p)
                    print ('Waktu penggunaan berakhir pada pukul ', v.struct(pilihan))
                else:
                    print("\nPilihan invalid......!\n")
                    continue

        elif number == 3:
            v.exit(60)
            break
        else:
            print("\nPilihan invalid......!\n")
            continue
        try:
            exit=eval(input("\nKlik 1 untuk melanjutkan :"))    
        except(SyntaxError,NameError):
            v.exit(60)
            break
        if exit!=1:
            v.exit(60)
            break
Warnet()
