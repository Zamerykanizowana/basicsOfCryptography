import random
import math

def c_print(string, mode):
    if mode == 'err':
        print('\x1b[31m' + str(string) + '\x1b[0m')
    elif mode == 'res':
        print('\x1b[32m' + str(string) + '\x1b[0m')
    elif mode == 'war':
        print('\x1b[33m' + str(string) + '\x1b[0m')
    elif mode == 'debb':
        print('\x1b[34m' + str(string) + '\x1b[0m')
    elif mode == 'debv':
        print('\x1b[35m' + str(string) + '\x1b[0m')
    elif mode == 'tit':
        print('\x1b[36m' + str(string) + '\x1b[0m')


def prime_number(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

def generate_key():
    c_print('----------Key generator------------', 'tit')
    p = 0
    while not prime_number(p):
        p = random.randint(30,200)
    q = 0
    while not prime_number(q):
        q = random.randint(30,200)
    c_print(f'p: {p}', 'debb')
    c_print(f'q: {q}', 'debb')
    n = p * q
    c_print(f'n: {n}', 'debb')
    fi_n = (p-1)*(q-1)
    c_print(f'fi_n: {fi_n}', 'debb')
    e = 0
    while not prime_number(e) or not math.gcd(e, fi_n) == 1:
        e = random.randint(0,300)
    c_print(f'e: {e}', 'debb')

generate_key()
