import os

import Class as v

menu = ["[1] Login"," [2] Logout"," [3] Warnet Tutup"]


class Warnet : 
    jls_extract_var = menu
    v.menu(" SILAKAN PILIH MENU ", jls_extract_var, 60)
    number= eval(input("\nMasukkan pilihan :"))
    if number == 1 :
        v.welcome("Ingin merental berapa jam?",60)
        jam = eval(input())
    

    

    
warnet = Warnet()
