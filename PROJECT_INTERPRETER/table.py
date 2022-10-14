def header(s, w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(s).center(w, '░') + '┃')
    print('┡' + ('━' * w)                       + '┩')

def header2Rows(s, s2, w):
    print('┏' + ('━' * w)                       + '┓')
    print('┃' + ' {} '.format(s).center(w, '░') + '┃')
    print('┃' + ' {} '.format(s2).center(w, '░')+ '┃')
    print('┡' + ('━' * w)                       + '┩')

def addRow(s, w):
    print('│' + ' {} '.format(s).ljust(w, ' ') + '│')

def addIterRow(n, s, w):
    if(n > 9):
        w -= 1

    print('│ {}❫ {} │'.format(str(n), s.ljust(w, ' ')), end = '\n')


def addCenterRow(s, w):
    print('│' + ' {} '.format(s).center(w, ' ') + '│')

def addSpecialRow(s, w):
    ls = s[:27]

    if len(s) == 15 or len(s) == 34:
        ls, w = s[:25], 54
    elif len(s) == 42:
        ls, w = s[:26], 58
    elif len(s) == 50:
        ls, w = s[:12], 49 
    elif len(s) == 21:
        ls, w = s[:8], 57
    elif len(s) == 13:
        w = 58
    elif len(s) == 14:
        w = 47
    elif len(s) == 5:
        w = 55

    print('│' + ' {} '.format(ls).center(w, ' ') + '│')

def spaceRow(w):
    print('│' + (' ' * w)                       + '│')

def sectionRow(w):
    print('╞' + ('═' * w)                       + '╡')

def endRow(w):
    print('└' + ('─' * w)                       + '┘')

def messageBox(s, w):
    print('┌' + ('─' * w)                       + '┐')
    print('│' + '{}'.format(s).center(w, ' ')   + '│')
    print('└' + ('─' * w)                       + '┘')

def warningBox(s, w):
    print('╭' + ('─' * w)                       + '╮')
    print('│' + '{}'.format(s).center(w, ' ')   + '│')
    print('╰' + ('─' * w)                       + '╯')