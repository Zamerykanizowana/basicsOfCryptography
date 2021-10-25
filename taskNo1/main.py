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
    test = val.count('1')
    print(f'Test no. 1: number of 1: {test}')
    if test > 9725 and test < 10275:
        print('Test no. 1 passed')
    else:
        print('Test no. 1 failed')

def testLenghtOfSeries(val):
    if len(val) > 0:
        tab_series = [0,0,0,0,0,0]
        first = val[0]
        check = 1

        for ele in val[1:]:
            print(f'ele: {ele}')
            if first == ele:
                check += 1
            else:
                tab_series[check-1] += 1
                first = ele
                check = 1
            print(f'check: {check}')
            print(f'Test no. 2: {tab_series}')
        tab_series[check-1] += 1
        print(f'check final: {check}')
        print(f'Test no.2 final: {tab_series}')
    else:
        print('String is empty!')

test_string= ''
testLenghtOfSeries(test_string)

n = 311*431
print(f'Blum number: {n}' if isBlumInteger(n) else f'Not Blum number: {n}')

a = int('0011111010110000100101010111001010100101001011010101110100010111100001110111101111111111111001001011011010100001001110110000100000110001100111011001100101001101110000110100001010010011010001110001100011010000000011001100010001100101011011000111110001101111001001000', 2)
print(f'Radom number: {a}')

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
