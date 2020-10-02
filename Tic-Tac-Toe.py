import random
import os
import copy
import sys

def LengthOfSquare(data):
    leng = []
    for x in range(tic):
        for y in range(tic):
            if data[x][y] not in ('O', 'X'):
                leng.append((x, y))
    return leng

def cetakPapan(data, par):
    print('+---------'*par,'+', sep='')
    for x in range(par):
        print('|         ' * par,'|',sep='')
        for y in range(par):
            if len(str(data[x][y])) > 1:
                jr = len(str(data[x][y]))
                tng = (9 - jr - 1) / 2

                if jr % 2 != 0:
                    min = round(tng)
                    max = round(tng) + 1
                else:
                    min = round(tng)
                    max = round(tng)

                print('|',' '*min + str(data[x][y]) + ' '*max, end='')
            else:
                print('|    ' + str(data[x][y]) + '    ', end='')
        print('|')
        print('|         '*par, '|', sep='')
        print('+---------'*par,'+', sep='')

def playerTurn(data, jm):
    turn = False
    while not turn:
        _input = int(input('Chose one of all number in the table : '))
        maxnum = jm * jm
        turn = _input >= 1 and _input <= maxnum

        if not turn:
            print('You must enter one of each number on the table !')
            continue

        num = _input - 1
        x = num // jm
        y = num % jm
        key = data[x][y]
        turn = key not in ['X', 'O']

        if not turn:
            print('That number already chosed')
            continue

    data[x][y] = 'O'   

def botTurn(data, jm):
    dah = LengthOfSquare(data)
    lang = len(dah)
    if lang > 0:
        rand = random.randrange(lang)
        x, y = dah[rand]
        data[x][y] = 'X'

def pemenang(data, smb, jml):
    if smb == 'X':
        win = 'bot'
    elif smb == 'O':
        win = 'you'
    else:
        win = None

    cross1 = cross2 = True
    _data = copy.deepcopy(data)

    for i in range(jml):
        for x in range(jml):
            if data[i][x] == smb:
                _data[i][x] = True
            else:
                _data[i][x] = False

    _baris = copy.deepcopy(_data)
    for i in range(jml):
        status = _data[i][0]
        for j in range(jml - 1):
            status = status and _data[i][j + 1]
        _baris[i] = status

    _kolom = copy.deepcopy(_data)
    for i in range(jml):
        status = _data[0][i]
        for j in range(jml - 1):
            status = status and _data[j + 1][i]
        _kolom[i] = status

    for i in range(jml):
        if data[i][i] != smb:
            cross1 = False
        if data[i][(jml - 1) - i] != smb:
            cross2 = False

    if True in _baris:
        return win
    elif True in _kolom:
        return win
    elif cross1 == True or cross2 == True:
        return win
    else:
        return None

tic = int(input('Masukan Dimensi Kolom (min 3, maks 9) : '))

if tic < 3 or tic > 9:
    print('Pastikan dimensi memenuhi syarat')
    sys.exit()

data = [
    [tic * x + y + 1 for y in range(tic)]
    for x in range(tic)
]

tac = random.randint(0, tic - 1)
toe = random.randint(0, tic - 1)
data[tac][toe] = 'X'

leng = LengthOfSquare(data)
player = True
while len(leng):
    cetakPapan(data, tic)
    if player:
        playerTurn(data, tic)
        winner = pemenang(data, 'O', tic)
        os.system('cls')
    else:
        botTurn(data, tic)
        winner = pemenang(data, 'X', tic)
        os.system('cls')
    
    if winner != None:
        break

    player = not player
    leng = LengthOfSquare(data)

cetakPapan(data, tic)
if winner == 'bot':
    print('You Lose !')
elif winner == 'you':
    print('You won')
else:
    print('Tie !')