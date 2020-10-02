import copy, string, random, os, keyboard, time, sys
from pynput.keyboard import Key, Listener 

def mulai(jml):
    dim = [
            [jml * j + i + 1 for i in range(jml)]
            for j in range(round(jml / 2))
          ]    
    ret = data_char(dim, jml)
    print_papan(ret, jml, 'before')
    print()
    playing(ret, jml)
    
def playing(data, jml, newlist=[]):
    param = []
    if len(newlist) != 0:
        os.system('cls')
        print_papan(data, jml, 'playing', param, newlist)
    checking_list(newlist, jml)
    backing = copy.deepcopy(data) 
    for i in range(len(data)):
        backing[i] = ''.join(data[i])
    backing = ''.join(backing)
    ent1 = False
    ent2 = False
    while not ent1:
        try: 
            inp1 = int(input('Masukan angka ke-1 : '))
            if (inp1 == 0 or inp1 > len(backing)) or inp1 in newlist:
                print('Pastikan memasukan angka yang tepat')
            else:
                while not ent2:
                    try:
                        inp2 = int(input('Masukan angka ke-2 : '))
                        if inp2 == inp1 or inp2 in newlist or (inp2 == 0 or inp2 > len(backing)):
                            print('Angka yang anda masukan sama !!!')
                            ent1 = True
                        elif inp2 == 0 or inp2 > len(backing):
                            print('Pastikan memilih angka yang tertera !!!')
                            ent1 = True
                        else:
                            ent1 = True
                            ent2 = True
                    except:
                        print('Pastikan memasukan angka !!!')
        except:
            print('Pastikan memasukan angka !!!')
            
    param.append(inp1)
    param.append(inp2)
    print_papan(data, jml, 'playing' ,param , newlist)
                             
def print_papan(val, data, mode, param=[], mylist=[]):
    os.system('cls')
    for i in range(data):
        print('+-----'*data, end='+\n')
        print('|     '*data, end='|\n')
        for j in range(data):
            if mode == 'before':
                print('|  '+str(val[i][j])+'  ', end='')
            elif mode == 'playing' and len(mylist) != 0:
                if data * i + j + 1 in (param) or data * i + j + 1 in mylist:
                    print('|  '+str(val[i][j])+'  ', end='')
                else:   
                    if len(str(data * i + j + 1)) > 1:
                        print('|  '+str(data * i + j + 1)+' ', end='')
                    else:
                        print('|  '+str(data * i + j + 1)+'  ', end='')
            elif mode == 'playing' and len(mylist) == 0:
                if data * i + j + 1 in (param):
                    print('|  '+str(val[i][j])+'  ', end='')
                else:   
                    if len(str(data * i + j + 1)) > 1:
                        print('|  '+str(data * i + j + 1)+' ', end='')
                    else:
                        print('|  '+str(data * i + j + 1)+'  ', end='')
            else:
                if len(str(data * i + j + 1)) > 1:
                    print('|  '+str(data * i + j + 1)+' ', end='')
                else:
                    print('|  '+str(data * i + j + 1)+'  ', end='')
        print('|', end ='\n')
        print('|     '*data, end='|')
        print()
    print('+-----'*data, end='+')
    print()
    
    newlist = mylist
    
    if mode == 'playing':
        if len(param) != 0:    
            a = int(param[0]) - 1
            b = int(param[1]) - 1
            
            a1 = a // data
            a2 = a % data
            b1 = b // data
            b2 = b % data
            
            if val[a1][a2] == val[b1][b2]:
                newlist.append(a + 1)
                newlist.append(b + 1)
            else:
                print('Inputan tidak sama ! Coba Lagi !!!')
        
            starttime = time.time()
            time.sleep(3.0 - ((time.time() - starttime) % 3.0))
            playing(val, data, newlist)
    elif len(param) == 0 and mode != 'after':
        print('You have '+str(data)+' second to remember it !!!')
        starttime = time.time()
        time.sleep(float(data) - ((time.time() - starttime) % float(data)))
        print_papan(val, data, 'after')

def data_char(data, jml):    
    for i in range(round(jml / 2)):
        for j in range(jml):
            data[i][j] = random.choice(string.ascii_letters).upper()
    
    x = copy.deepcopy(data)
    for i in range(len(data)):
        x[i] = ','.join(data[i])
    x = ','.join(x)
    for j in range(len(data)):
        for k in range(len(data[j])):
            if x.count(data[j][k]) >= 2:
                done = False
                while not done:
                    ganti = random.choice(string.ascii_letters).upper()
                    if x.count(ganti) == 0:
                        data[j][k] = ganti
                        done = True
    data *=2    
    y = copy.deepcopy(data)
    for z in range(len(data)):
        y[z] = ''.join(data[z])
          
    for i in range(len(y)):
        y = ''.join(y)
    y = list(y)
    random.shuffle(y)
    new_data = []
    for i in range(len(data)):
        isi = [y[z] for z in range(jml * i, jml * (i + 1))]
        new_data.append(isi)
        
    return new_data
    
def checking_list(mylist, jml):
    if len(mylist) == jml*jml:
        print('Congratulations, You won !!!')
        sys.exit()

dah = False
print('Pilih Level : ')
print('1. Easy')
print('2. Medium')
print('3. Hard')
print()
while not dah:
    try: 
        pil = int(input('Masukan Pilihan :'))
        if pil == 1:
            pil = 4
            dah = True
        elif pil == 2:
            pil = 6
            dah = True
        elif pil == 3:
            pil = 8
            dah = True
        else:
            print('Pastikan Memasukan angkat yang tertera !')
    except ValueError:
        print('Pastikan Memasukan angka')

mulai(pil)