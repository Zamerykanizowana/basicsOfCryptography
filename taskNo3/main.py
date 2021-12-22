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
    while True:
        p = random.randint(1000,2000)
        if prime_number(p):
            break
    while True:
        q = random.randint(1000,2000)
        if prime_number(q):
            break
    #p = 31
    #q = 19
    #adam
    #p = 503
    #q = 1373
    print(c_str(f'p: {p}', 'deb'))
    print(c_str(f'q: {q}', 'deb'))
    n = p * q
    print(c_str(f'n: {n}', 'deb'))
    fi_n = (p-1)*(q-1)
    print(c_str(f'fi_n: {fi_n}', 'deb'))
    while True:
        e = random.randint(0,fi_n-1)
        if prime_number(e) and math.gcd(e, fi_n) == 1:
            break
    #e = 7
    #e = 642011
    # e, d, n
    print(c_str(f'e: {e}', 'deb'))
    d, _ = xea(e,fi_n)
    d = d%fi_n
    print(c_str(f'd: {d}', 'deb'))
    print(c_str(f'public key: {e} and {n}, private key: {d} i {n}', 'res'))
    return e, n, d
    

def encrypt(e, n, m):
    c = (m**e) % n
    #print(c_str(f'encrypt message c: {c}','res'))
    return c

def decrypt(d, n, c):
    m = c**d % n
    #print(c_str(f'decrypted message: m: {m}', 'res'))
    return m

def check_en_de_m(m, de_m):
    if m == de_m:
        print(c_str('Message was correctly encrypted decrypted.', 'res'))
        return True
    else:
        print(c_str('Message was NOT correctly encrypted decrypted.', 'err'))
        return False

def check_s_ver(s, ver_s):
    if s == ver_s:
        print(c_str('Message was correctly signed and verified.', 'res'))
        return True
    else:
        print(c_str('Message was NOT correctly signed and verified.', 'err'))
        return False


def question(len_of_m):
    question = input(c_str('Press m if manual message to encrypt, press a to automatic\n','inte'))
    if question == 'a':
        m = ''
        while len(m) < len_of_m:
            m = m +  chr(random.randint(33,122))
    elif question == 'm':
        m = ''
        m = input(c_str('Select number from 1 to 9999\n', 'inte'))
    print(c_str(f'length of m: {len(m)}', 'deb'))
    print(c_str(f'm: {m}', 'deb'))
    return m



e, n, d = generate_key()

m = question(50)
#
tab_c = []
for sig in m:
    tab_c.append(encrypt(e, n, ord(sig)))
print(c_str(f'tab_c: {tab_c}', 'res'))

de_m = ''
for ele in tab_c: 
    de_m = de_m + chr(decrypt(d, n, ele))

print(c_str(f'de_m: {de_m}', 'res'))
check_en_de_m(m, de_m)

print(c_str('---------------Singature---------------', 'tit'))
e_a, n_a, d_a = generate_key()
e_b, n_b, d_b = generate_key()

m_for_sig = question(20)
tab_a = []
tab_b = []
for sig in m_for_sig:
    tab_a.append(encrypt(d_a, n_a, ord(sig)))
    tab_b.append(encrypt(d_b, n_b, ord(sig)))
print(c_str(f'tab_a: {tab_a}', 'res'))
print(c_str(f'tab_b: {tab_b}', 'res'))

de_m_a = ''
de_m_b = ''
for i in range(0, len(tab_a)):
    print(f'i: {i} tab_a[i]: {tab_a[i]} tab_b[i]: {tab_b[i]}')
    de_m_a = de_m_a + chr(decrypt(e_a, n_a, tab_a[i]))
    de_m_b = de_m_b + chr(decrypt(e_b, n_b, tab_b[i]))
print(c_str(f'de_m_a: {de_m_a}', 'res'))
print(c_str(f'de_m_b: {de_m_b}', 'res'))
check_s_ver(m_for_sig, de_m_a)
check_s_ver(m_for_sig, de_m_b)



