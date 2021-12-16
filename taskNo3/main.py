import random
import math

def c_str(string, mode):
    if mode == 'err':
        return '\x1b[31m' + str(string) + '\x1b[0m'
    elif mode == 'res':
        return '\x1b[32m' + str(string) + '\x1b[0m'
    elif mode == 'war':
        return '\x1b[33m' + str(string) + '\x1b[0m'
    elif mode == 'deb':
        return '\x1b[34m' + str(string) + '\x1b[0m'
    elif mode == 'inte':
        return '\x1b[35m' + str(string) + '\x1b[0m'
    elif mode == 'tit':
        return '\x1b[36m' + str(string) + '\x1b[0m'

def prime_number(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

def xea(e, fi):
    if e == 0:
        return 0, 1
    x, y = xea(fi%e,e)
    return y-(fi//e)*x, x


def generate_key():
    print(c_str('----------Key generator------------', 'tit'))
    p = 0
    while not prime_number(p):
        p = random.randint(1,100)
    q = 0
    while not prime_number(q):
        q = random.randint(1,100)
    p = 31
    q = 19
    print(c_str(f'p: {p}', 'deb'))
    print(c_str(f'q: {q}', 'deb'))
    n = p * q
    print(c_str(f'n: {n}', 'deb'))
    fi_n = (p-1)*(q-1)
    print(c_str(f'fi_n: {fi_n}', 'deb'))
    e = 0
    while not prime_number(e) or not math.gcd(e, fi_n) == 1:
        e = random.randint(0,200)
    e = 7
    print(c_str(f'e: {e}', 'deb'))
    d, _ = xea(e,fi_n)
    d = d%fi_n
    print(c_str(f'd: {d}', 'deb'))
    print(c_str(f'public key: {e} and {n}, private key: {d} i {n}', 'res'))
    return e, n, d
    

def encrypt(e, n):
    question = input(c_str('Press m if manual message to encrypt, press a to automatic\n','inte'))
    if question == 'a':
        m = random.randint(1,9999)
        m = 8
    elif question == 'm':
        m = 0
        while m < 1 or m > 9999:  
            m = int(input(c_str('Select number from 1 to 9999\n', 'inte')))
    print(c_str(f'm: {m}', 'deb'))
    c = (m**e) % n
    print(c_str(f'encrypt message c: {c}','res'))
    return c

def decrypt(d, n, c):
    m = c**d % n
    print(c_str(f'decrypted message: m: {m}', 'res'))
    return m

e, n, d = generate_key()
print(f'{e}, {n}, {d}')
c = encrypt(e, n)
print(f'{c}')
m = decrypt(d, n, c)
