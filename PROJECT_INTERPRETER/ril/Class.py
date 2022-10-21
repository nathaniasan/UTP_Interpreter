from operator import truediv
from threading import get_ident
import dc_data_member as data
import time


def struct(jam):
    a=time.localtime()
    hr=a.tm_hour + jam
    mn=a.tm_min
    sc=a.tm_sec
    return ('{}:{}:{}'.format(hr,mn,sc))

def welcome(s,x,w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(s).center(w, '░') + '┃')
    print('┃' + ' {} '.format("Berikut beberapa paket penyewaan").center(w, '░') + '┃')
    print('┃' + ' {} '.format(x).center(w, '░') + '┃')
    print('┃' + ' {} '.format("Jika sudah memiliki member silahkan login di pilihan 2").center(w, '░') + '┃')
    print('┃' + ' {} '.format("Terima Kasih :-)").center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')

def menu(c,s,w):
    print('┏' + ('━' * w)                       + '┓')
    print('┏' + (' ' * w)                       + '┓')
    print('┃' + ' {} '.format(c).center(w, '░') + '┃')
    print('┃' + ' {} '.format(s).center(w, '░') + '┃')
    print('┏' + (' ' * w)                       + '┓')

    print('┡' + ('━' * w)                       + '┩')

def pembayaran(p):
    while True:
        while True:
                try:
                    pembayaran=eval(input("Masukan nominal pembayaran :"))
                except (SyntaxError,NameError):
                    print("pilihan invalid")
                    continue
                break
        if p==1:
            if pembayaran==5000:
                print("Pembayaran berhasil")
                break
            elif pembayaran>5000:
                print("Pembayaran berhasil")
                print("Kembalian anda : ",pembayaran-5000)
                break
            elif pembayaran<5000:
                print("Pembayaran Invalid")
        elif p==2:
            if pembayaran==9000:
                print("Pembayaran berhasil")
                break
            elif pembayaran>9000:
                print("Pembayaran berhasil")
                print("Kembalian anda : ",pembayaran-9000)
                break
            elif pembayaran<9000:
                print("Pembayaran Invalid")
        elif p==3:
            if pembayaran==13000:
                print("Pembayaran berhasil")
                break
            elif pembayaran>13000:
                print("Pembayaran berhasil")
                print("Kembalian anda : ",pembayaran-13000)
                break
            elif pembayaran<13000:
                print("Pembayaran Invalid!!")

def pembayaranMember(p):
    while True:
        while True:
                try:
                    pembayaran=eval(input("Masukan nominal pembayaran :"))
                except (SyntaxError,NameError):
                    print("pilihan invalid")
                    continue
                break
        if p==1:
            if pembayaran==4000:
                print("Pembayaran berhasil")
                break
            elif pembayaran>4000:
                print("Pembayaran berhasil")
                print("Kembalian anda : ",pembayaran-4000)
                break
            elif pembayaran<4000:
                print("Pembayaran Invalid")
        elif p==2:
            if pembayaran==7000:
                print("Pembayaran berhasil")
                break
            elif pembayaran>7000:
                print("Pembayaran berhasil")
                print("Kembalian anda : ",pembayaran-7000)
                break
            elif pembayaran<7000:
                print("Pembayaran Invalid")
        elif p==3:
            if pembayaran==10000:
                print("Pembayaran berhasil")
                break
            elif pembayaran>10000:
                print("Pembayaran berhasil")
                print("Kembalian anda : ",pembayaran-10000)
                break
            elif pembayaran<10000:
                print("Pembayaran Invalid!!")

def indexMember(id,ps):
    for i in range (1,4):
        if id==data.id[i] and ps==data.ps[i]:
            return i
    return 0

def login(w):

    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format("Login Member Warnet PI").center(w, '░') + '┃')
    print('┃' + ' {} '.format("silahkan masukan id password dengan benar").center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')
 
    while True:
        id=input("id :")
        ps=input("password :")
        memberIndex=indexMember(id,ps) 
        if memberIndex==0:
            print("Login gagal! id atau password salah!")
        else:
            print("Login berhasil..................!")
            break

    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format("Selamat datang ").center(w, '░') + '┃')
    print('┃' + ' {} '.format(data.nama[memberIndex]).center(w, '░') + '┃')
    print('┃' + ' {} '.format(data.jenis[memberIndex]).center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')

def exit(w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format("Terima kasih ").center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')
