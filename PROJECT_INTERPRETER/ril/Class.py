def welcome(s, w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(s).center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')

def menu(c,s,w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(c).center(w, '░') + '┃')
    print('┃' + ' {} '.format(s).center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')
