from datetime import datetime, timedelta
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from copy import deepcopy
import csv
import main

def aes_all(mode, message, k, i_vector):
    time_en = 0
    time_de = 0
    #print(f'aes_all: message: {message}')
    for ele in message:
        if mode == 'ecb':
            start = datetime.now()
            en_mess = AES.new(key = k, mode = AES.MODE_ECB).encrypt(ele)
            stop_en = datetime.now()
            de_mess = AES.new(key = k, mode = AES.MODE_ECB).decrypt(ele)
            stop_de = datetime.now()
        elif mode == 'cbc':
            start = datetime.now()
            en_mess = AES.new(key = key, mode = AES.MODE_CBC, iv = i_vector).encrypt(ele)
            stop_en = datetime.now()
            de_mess = AES.new(key = key, mode = AES.MODE_CBC, iv = i_vector).decrypt(ele)
            stop_de = datetime.now()
        elif mode == 'ctr':
            start = datetime.now()
            en_mess = AES.new(key = key, mode = AES.MODE_CTR).encrypt(ele)
            stop_en = datetime.now()
            de_mess = AES.new(key = key, mode = AES.MODE_CTR).decrypt(ele)
            stop_de = datetime.now()
        elif mode == 'cfb':
            start = datetime.now()
            en_mess = AES.new(key = key, mode = AES.MODE_CFB,segment_size=8*16).encrypt(ele)
            stop_en = datetime.now()
            de_mess = AES.new(key = key, mode = AES.MODE_CFB,segment_size=8*16).decrypt(ele)
            stop_de = datetime.now()
        elif mode == 'ofb':
            start = datetime.now()
            en_mess = AES.new(key = key, mode = AES.MODE_OFB).encrypt(ele)
            stop_en = datetime.now()
            de_mess = AES.new(key = key, mode = AES.MODE_OFB).decrypt(ele)
            stop_de = datetime.now()
        elif mode == 'openpgp':
            start = datetime.now()
            en_mess = AES.new(key = key, mode = AES.MODE_OPENPGP).encrypt(ele)
            stop_en = datetime.now()
            de_mess = AES.new(key = key, mode = AES.MODE_OPENPGP).decrypt(ele)
            stop_de = datetime.now()
        else:
            print('Somthing went wrong :(')
        time_en = time_en +  timedelta.total_seconds(stop_en-start)
        time_de += timedelta.total_seconds(stop_de-stop_en)
        #print(f'\x1b[34mtime_en: {time_en}\x1b[0m')
        #print(f'\x1b[35mtime_de: {time_de}\x1b[0m')
    print(f'end of def: time_en: {time_en} and time_de: {time_de}')
    return round(time_en, 5), round(time_de,5), round(time_en + time_de,5)
        

result = []

a = b'Lorem ipsum'
b = b'asdfghjklmbvcxzasdfghjkloiuytrewqsdfghjkmnbvcxswertguyfr57689ijbvcs436e7r8ohbvgfyt23456@$&*(YGVBNKvgcjbd'
f = open('../taskNo1/hp_chapter1.txt', 'r')
c = bytes(f.read(), 'utf-8')
print(f'Length of a: {len(a)}')
print(f'Length of b: {len(b)}')
print(f'Length of c: {len(c)}')

key = b'djirko9$d,-)12se'
i_vector = b'trw4^m.a/0wNY#xq'

messages_to_en_de = []
for ele in [a,b,c]:
    messages_to_en_de.append(main.chunk(pad(ele,16),16))


tab_time_all = []
tab_time_row = []

modes = ['ecb', 'cbc', 'ctr', 'cfb', 'ofb', 'openpgp']
   
for mode in modes:
    tab_time_row.append(mode)
    for ele in messages_to_en_de:
        tmp = aes_all(mode, ele, key, i_vector)
        for t in tmp:
            tab_time_row.append(t)
    tab_time_all.append(tab_time_row)
    tab_time_row = []

print('-----------------------------------')
print(tab_time_all)

with open('time.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for ele in tab_time_all:
        spamwriter.writerow(ele)

csvfile.close()
