import os
import Class as v
menu = ["[1] Login"," [2] Logout"," [3] Warnet Tutup"]

class Warnet : 
    v.menu(" SILAKAN PILIH MENU ", *menu , 60)
    

    def dislogin(data_dislogin, number):
        os.system("cls")
    print('Maaf kursi nomor', (number+1), 'saat ini sedang dipakai')
    print(f"{'Kursi':7} {'Status':9} {'Username':12} {'Mulai':12}")
    print("{0:^5} {1:1} {2:9} {3:12} {4:12}".format(data_dislogin[number]["Kursi"]," ",data_dislogin[number]["Status"],data_dislogin[number]["Username"],data_dislogin[number]["Mulai"]))
    enter = input("Tekan [Enter] untuk kembali")
    print(enter)


def dislogout(data_dislogout, number):
    os.system("cls")
    print('Maaf, tidak ada user pada kursi nomer', (number+1))
    print(f"{'Kursi':7} {'Status':9} {'Username':12} {'Mulai':12}")
    print("{0:^5} {1:1} {2:9} {3:12} {4:12}".format(data_dislogout[number]["Kursi"]," ",data_dislogout[number]["Status"],data_dislogout[number]["Username"],data_dislogout[number]["Mulai"]))
    enter = input("Tekan [Enter] untuk kembali")
    print(enter)


def common():
    os.system("cls")
    print(f"{'SISTEM OPERATOR WARNET Kampung Baru':^50}")
    print("-"*50)
    print(f"{'Kursi':9} {'Status':11} {'Username':20s}")
    print("-"*50)
    for table in data_user:
        print("{0:^5} {1:3} {2:11} {3:20}".format(table["Kursi"]," ",table["Status"],table["Username"]))

    warnet = Warnet()
