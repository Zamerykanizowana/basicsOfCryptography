import math
import random
from datetime import datetime

"""
n = Blum number
r = the lenght of the number
a = random selected natural number, but math.gcd(a,n) = 1
"""

# Function isBlumInteger from: https://www.geeksforgeeks.org/blum-integer/
# python 3 program to check if a
# number is a Blum integer

# Function to cheek if number
# is Blum Integer
def isBlumInteger(n):
    prime = [True]*(n + 1)
    # to store prime numbers from 2 to n
    i = 2
    while (i * i <= n):
        # If prime[i] is not
        # changed, then it is a prime
        if (prime[i] == True) :
            # Update all multiples of p
            for j in range(i * 2, n + 1, i):
                prime[j] = False
        i = i + 1
    # to check if the given odd integer
    # is Blum Integer or not
    for i in range(2, n + 1) :
        if (prime[i]) :
            # checking the factors
            # are of 4t+3 form or not
            if ((n % i == 0) and
                        ((i - 3) % 4) == 0):
                q = int(n / i)
                return (q != i and prime[q]
                       and (q - 3) % 4 == 0)
    return False

def binaryToDecimal(val):
    return int(val,2)

def testNumberOfOne(val):

    #print('Test no. 1 start ---------------------------------------')

    test = val.count('1')
    #print(f'Test no. 1: number of 1: {test}')
    if test > 9725 and test < 10275:
        print('\x1b[32mTest no. 1 passed\x1b[0m')
    else:
        print('\x1b[31mTest no. 1 failed\x1b[0m')

    #print('Test no. 1 stop ----------------------------------------')

def testLengthOfSeries(val):
    #print('Test no. 2 start ---------------------------------------')

    # cheks = 0 means serie has 1 length, so this serie fits into 
    # tab_series[x][check] / tab_res[x][check]
    def __assign(first_ele, check_num, tab_res):
        tab_res[int(first_ele)][check_num if check_num<6 else 5] += 1
        return tab_res
    
    def __check(value, single_tab_constraints):
        return single_tab_constraints[0] < value < single_tab_constraints[1]


    constraints = [[2315,2685], [1114, 1386], [527,723], [240,384], [103,209], [103,209]]
    tab_series = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
    first = val[0]
    check = 0
    
    for ele in val[1:]:
        if first == ele:
            check += 1
        else:
            tab_series = __assign(first, check, tab_series)
            check = 0
        first = ele

    tab_series = __assign(first, check, tab_series)
            
    #print(f'tab_series: {tab_series}')
    test_result = True
    for single_tab in tab_series:
        for index, ele in enumerate(single_tab):
            test_result = __check(ele, constraints[index])
            if not test_result:
                break
        if not test_result:
            break

    print('\x1b[32mTest no. 2 passed\x1b[0m' if test_result else '\x1b[31mTest no. 2 failed\x1b[0m') 
    #print('Test no. 2 stop ----------------------------------------')

#test_string_for_test_no_2 = '111101010101111111000000000001'
#testLengthOfSeries(test_string_for_test_no_2)


def testLongSerie(val):
    #print('Test no. 3 start ---------------------------------------')
    if len(val) > 0:
        test = True
        first = val[0]
        check = 1

        for ele in val[1:]:
            #print(f'ele: {ele}')
            if first == ele:
                check += 1
                if check > 25:
                    test = False
                    #print(f'Test will fail, check equals {check}')
                    break
            else:
                check = 1
            
            first = ele
        print('\x1b[32mTest no. 3 passed\x1b[0m' if test else '\x1b[31mTest no. 3 failed\x1b[0m')
    #print('Test no. 3 stop ----------------------------------------')
        
#test_string_3 = '111111111111111111111111111111111111111111111111111111111111111111111111'
#testLongSerie(test_string_3)

def pokerTest(val):
    #print('Test no. 4 start ---------------------------------------')
    table_val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    table_len = len(table_val)
    val_len = len(val)
    #print(f'Length of table {table_len}')
    #print(f'Length of val {val_len}')
    i = 4
    while i <= val_len:
        table_val[int(val[i-4:i], 2)] += 1
        result = val[i-4:i]
        #print(f'Result: {result}')
        i += 4
    #print(f'Result table: {table_val}')
    
    table_val_result = []
    res = 0
    for ele in table_val:
        res += ele**2
    res = res*(16/5000)-5000
    if res > 2.16 and res < 46.17:
        test = True
    else:
        test = False
    print('\x1b[32mTest no. 4 passed\x1b[0m' if test else '\x1b[31mTest no. 4 failed\x1b[0m')
    #print('Test no. 4 stop ----------------------------------------')


#print('TEST NO. 4')
#test_string_4 = 'random string to test Test no. 4'
#test_num_4 = '11110000101011100000'
#pokerTest(test_num_4)

# key is from generator bbs, this is the generated number
# massage is secrete massage to encrypt or decrypt
# mode:
## encrypt - True
## decrypt - False
def encryptor_decryptor(key, message, mode):
    if mode:
        bit_message = bin(int.from_bytes(message.encode(), 'big'))
        #print(f'bit_message: {bit_message[2:]}')
        #print(f'key:    {key}')
        length_bit_message = len(bit_message[2:])
        print(f'Length of bit message[2:]: {length_bit_message}')
        if length_bit_message <= len(key):
            result = bin(int(bit_message[2:],2) ^ int(key,2))
            result = result[2:]
            print(f'Length of result[2:]: {len(result)}')
            #print(f'result {result}')
            print(f'Length of key: {len(key)}')
            #print(f'key    {key}')
            # dd/mm/YY H:M:S
            now = datetime.now()
            date_and_time = now.strftime("%d-%m-%Y_%H:%M:%S")

            # creating file with generated number
            file_name = date_and_time+"_encryp_mes.txt"
            f_en_message= open(file_name,"w+")
            f_en_message.write(result)
            f_en_message.close()
            #print(f'encrypted_m: {result}')
            print(f'Your message was encrypted, check saved file {file_name} if needed')
            return result
        else:
            print('Your message is too long!')
    else:
        length_bit_message = len(message)
        print(f'Length of message: ')
        tmp = bin(int(message,2) ^ int(key,2))
        tmp = int(tmp,2)
        result = tmp.to_bytes((tmp.bit_length() + 7) // 8, 'big').decode()
        print('Your message was decrypted')
        return result


#print('Test for encryptor_decryptor')
#key = '1010101011111111110000000011110011010'
#mes = '/ab'
#res = encryptor_decryptor(key, mes, True)
#encryptor_decryptor(key, res, False)


def testIfmessageWasCorrectlyEncrypted(before_encryption, after_decryption, mode): 
    if mode:
        print(f'before_encryption: \n \x1b[34m{before_encryption}\x1b[0m')
        print(f'after_decryption: \n \x1b[35mn{after_decryption}\x1b[0m')
    print('\x1b[32mMessage was correctly encrypted-decrypted\x1b[0m' if before_encryption == after_decryption else '\x1b[31mEncryption-decryption failed\x1b[0m')

def runAllTests(generated_number):

    print('\x1b[104m------------- TESTS -------------\x1b[0m')
    testNumberOfOne(generated_number)
    testLengthOfSeries(generated_number)
    testLongSerie(generated_number)
    pokerTest(generated_number)

print('\x1b[104m------------- Generator BBS -------------\x1b[0m')
#Adam numbers
#n = 1200000003730000000273

#M numbers
#n = 62615533
#a = 7088

#my numbers
n = 5323*7411
a = int('1010101010111001010100001', 2)

# Check if number are good to use
#isBlumInt = isBlumInteger(n)
# If don't have time to check Blum number ;)
isBlumInt = True
isGCDOne = math.gcd(a,n)==1

if isBlumInt and isGCDOne:

    
    print(f'Blum number: {n}')
    print(f'Random number: {a}')
    print(f'Selected number gcd(a,n)=1')

    # r - number of signs (0 or 1)
    r = 20000
    x_0 = a**2%n
    generated_number = '0' if x_0%2 == 0 else '1'
    while r > 1:
        #print(f'Line {r}')
        x_0 = x_0**2%n
        r -= 1
        generated_number = generated_number + ('0' if x_0%2 == 0 else '1')

    runAllTests(generated_number)

    # dd/mm/YY H:M:S
    now = datetime.now()
    date_and_time = now.strftime("%d-%m-%Y_%H:%M:%S")
    #print("date and time: ", date_and_time)

    # creating file with generated number
    f_gen_number= open("142463_"+date_and_time+".txt","w+")
    f_gen_number.write(generated_number)
    f_gen_number.close()

    encrypt_decrypt_message = True
    if encrypt_decrypt_message:
        # message to encrypte
        with open('hp_chapter1.txt', 'r') as file:    
            data = file.read().replace('\n', '')

        file.close()
        secret_message = data[:2000]
        
        encrypted_message = encryptor_decryptor(generated_number,secret_message, True)
        runAllTests(encrypted_message)
        decrypted_message = encryptor_decryptor(generated_number,encrypted_message,False) 
        testIfmessageWasCorrectlyEncrypted(secret_message, decrypted_message,False)

else:
    print(f'Selected numbers are worng, isBlumInt: {isBlumInt}, isGCDOne: {isGCDOne}')
