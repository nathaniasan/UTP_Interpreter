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

def kategori():
    
    print('┏' + ('━' * w)                       + '┓')
    print 
    print('┏' + (' ' * w)                       + '┓')

def pembayaran(p):
    while True:
        pembayaran=eval(input("Masukan nominal pembayaran :"))
        if p==1:
            if pembayaran==5000:
                break
            elif pembayaran>5000:
                print("Kembalian anda : ",pembayaran-5000)
                break
            elif pembayaran<5000:
                print("Pembayaran Invalid")
        elif p==2:
            if pembayaran==9000:
                break
            elif pembayaran>9000:
                print("Kembalian anda : ",pembayaran-9000)
                break
            elif pembayaran<9000:
                print("Pembayaran Invalid")
        elif p==3:
            if pembayaran==13000:
                break
            elif pembayaran>13000:
                print("Kembalian anda : ",pembayaran-13000)
                break
            elif pembayaran<13000:
                print("Pembayaran Invalid!!")

    
def headerlogin(w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format("Login Member Warnet PI").center(w, '░') + '┃')
    print('┃' + ' {} '.format("silahkan masukan id password dengan benar").center(w, '░') +'┃')
    print('┡' + ('━' * w)                       + '┩')

def member ():
    while True :
        try : 
            y = input ('nama anda adalah : ')
        except TypeError(y):
            print('silakan login ulang, daya yang anda masukkan salah')
            welcome(s, x, w)
