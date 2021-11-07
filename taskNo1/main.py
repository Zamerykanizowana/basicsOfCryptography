import math

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

    print('Test no. 1 start ---------------------------------------')

    test = val.count('1')
    print(f'Test no. 1: number of 1: {test}')
    if test > 9725 and test < 10275:
        print('Test no. 1 passed')
    else:
        print('Test no. 1 failed')

    print('Test no. 1 stop ----------------------------------------')

def testLenghtOfSeries(val):
    print('Test no. 2 start ---------------------------------------')

    if len(val) > 0:
        tab_series = [0,0,0,0,0,0]
        first = val[0]
        check = 1

        for ele in val[1:]:
            #print(f'ele: {ele}')
            if first == ele:
                check += 1
            else:
                if check < 7:
                    tab_series[check-1] += 1
                else:
                    tab_series[5] += 1
                check = 1
            
            first = ele
            #print(f'check: {check}')
            #print(f'Test no. 2: {tab_series}')
        if check < 7:
            tab_series[check-1] += 1
        else:
            tab_series[5] += 1

        #print(f'check final: {check}')
        print(f'Test no.2 final: {tab_series}')

        result = True
        print(f'test line tab_series {tab_series[0]}')
        if 2315 > tab_series[0] or tab_series[0] > 2685:
            result = False
        if 1114 > tab_series[1] or tab_series[1] > 1386:
            result = False
        if 527 > tab_series[2] or tab_series[2] > 723:
            result = False
        if 240 > tab_series[3] or tab_series[3] > 384:
            result = False
        if 103 > tab_series[4] or tab_series[4] > 209:
            result = False
        if 103 > tab_series[5] or tab_series[5] > 209:
            result = False
        print('Test no. 2 passed' if result else 'Test no. 2 failed')

    else:
        print('String is empty!')
    print('Test no. 2 stop ----------------------------------------')

#Test for test no. 2 :)
#test_string= '11111010101010111111111111111111111'
#testLenghtOfSeries(test_string)

def testLongSerie(val):
    print('Test no. 3 start ---------------------------------------')
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
                    print(f'Test will fail, check equils {check}')
            else:
                check = 1
            
            first = ele
        print('Test no. 3 passed' if test else 'Test no. 3 failed')
    print('Test no. 3 stop ----------------------------------------')
        
def pokerTest(val):
    print('Test no. 4 start ---------------------------------------')
    table_val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    table_len = len(table_val)
    val_len = len(val)
    print(f'Lenght of table {table_len}')
    print(f'Lenght of val {val_len}')
    i = 4
    while i <= val_len:
        table_val[int(val[i-4:i], 2)] += 1
        result = val[i-4:i]
        #print(f'Result: {result}')
        i += 4
    print(f'Result table: {table_val}')
    
    table_val_result = []
    res = 0
    for ele in table_val:
        res += ele**2
    res = res*(16/5000)-5000
    if res > 2.16 and res < 46.17:
        test = True
    else:
        test = False
    print('Test no. 4 passed' if test else 'Test no. 4 failed')
    print('Test no. 4 stop ----------------------------------------')


#print('TEST NO. 4')
#test_string_4 = 'random string to test Test no. 4'
#test_num_4 = '11110000101011100000'
#pokerTest(test_num_4)



n = 311*431
print(f'Blum number: {n}' if isBlumInteger(n) else f'Not Blum number: {n}')

a = int('1010001010110000110111011111010100010101100001110000011001101001010011001011000110101100111010100001', 2)
print(f'Random number: {a}')

print(f'Selected number gcd(a,n)=1' if math.gcd(a,n)==1 else 'Wrong number a')

r = 20000

x_0 = a**2%n
generated_number = '0' if x_0%2 == 0 else '1'
while r > 1:
    #print(f'Line {r}')
    x_0 = x_0**2%n
    r -= 1
    generated_number = generated_number + ('0' if x_0%2 == 0 else '1')

#print(bin(x_0))
#print('Generated number:')
#print(generated_number)
lenght = len(generated_number)
print(f'Test line: generated_number lenght: {lenght}')
testNumberOfOne(generated_number)
testLenghtOfSeries(generated_number)
testLongSerie(generated_number)
pokerTest(generated_number)
