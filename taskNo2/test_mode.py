from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from copy import deepcopy
import csv
import main

def aes_all(mode, ele, key, i_vector):
    if mode == 'ecb':
        start = datetime.now()
        en_mess = AES.new(key,MODE_ECB).encrypt(ele)
        stop_en = datetime.now()
        de_mess = AES.new(key,MODE_ECB).decrypt(ele)
        stop_de = datetime.now()
    elif mode == 'cbc':
        start = datetime.now()
        en_mess = AES.new(key,MODE_CBC,i_vector).encrypt(ele)
        stop_en = datetime.now()
        de_mess = AES.new(key,MODE_CBC,i_vector).decrypt(ele)
        stop_de = datetime.now()
    elif mode == 'ctr':
        start = datetime.now()
        en_mess = AES.new(key,MODE_CTR).encrypt(ele)
        stop_en = datetime.now()
        de_mess = AES.new(key,MODE_CTR).decrypt(ele)
        stop_de = datetime.now()
    elif mode == 'cfb':
        start = datetime.now()
        en_mess = AES.new(key,MODE_CFB,segment_size=8*16).encrypt(ele)
        stop_en = datetime.now()
        de_mess = AES.new(key,MODE_CFB,segment_size-8*16).decrypt(ele)
        stop_de = datetime.now()
    elif mode == 'ofb':
        start = datetime.now()
        en_mess = AES.new(key,MODE_OFB).encrypt(ele)
        stop_en = datetime.now()
        de_mess = AES.new(key,MODE_OFB).decrypt(ele)
        stop_de = datetime.now()
    elif mode == 'openpgp':
        start = datetime.now()
        en_mess = AES.new(key,MODE_OPENPGP).encrypt(ele)
        stop_en = datetime.now()
        de_mess = AES.new(key,MODE_OPENPGP).decrypt(ele)
        stop_de = datetime.now()
    return [(stop_en-start).total_second(), (stop_de-stop-en).total_second()]
        





with open('eggs.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

result = []

a = b'Lorem ipsum'
b = b'asdfghjklmbvcxzasdfghjkloiuytrewqsdfghjkmnbvcxswertguyfr57689ijbvcs436e7r8ohbvgfyt23456@$&*(YGVBNKvgcjbd'
f = open('../taskNo1/hp_chapter1.txt', 'r')
c = bytes(f.read(), 'utf-8')
print(f'Length of a: {len(a)}')
print(f'Length of b: {len(b)}')
print(f'Length of c: {len(c)}')

key = b'djirko9$d,-)12sbe'
i_vector = b'trw4^m.a/0wNY#xq'

messages_to_en_de = []
for ele in [a,b,c]:
    message_to_en_de.append(main.chunk(main.pad(ele,16),16))

tab_time_all = []
tab_time_row = []

modes = [MODE_ECB,MODE_CBC,MODE_CTR,MODE_CFB,MODE_OFB,MODE_OpenPGP]



for ele_m in message_to_en_de:
    start = datetime.now()
    stop_en = datetime.now()
    de_mess = AES.new(key,MODE_ECB).decrypt(en_mess)
    stop_de = datetime.now()
    tab_time_row.append((stop_en-start).total_seconds())
    tab_time_row.append((stop_de-stop_en).total_seconds())
    


