from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def ecb(m,k):
    print('hi')

def chunk(m, size):
    tab_res = []
    i = 0
    while i+size <= len(m):
        tab_res.append(m[i:i+size])
        i += size
    return tab_res
    
def encrypt_chunk(m, k):
    return AES.new(key=k, mode=AES.MODE_ECB).encrypt(m)

def decrypt_chunk(m, k):
    return AES.new(key=k, mode=AES.MODE_ECB).decrypt(m)

message_to_encrypt = b'I just want to finish this task and go to bed.'
cipherKey = b'oskm3ucjakops2LA'
print(f'length mes: {len(message_to_encrypt)}')
tmp_pan = pad(message_to_encrypt,16)
print(f'length pad(mes): {len(tmp_pan)}')
print(tmp_pan)

res = chunk(tmp_pan, 16)
print(res)
encrypted_message = []
for ele in res:
    encrypted_message.append(encrypt_chunk(ele,cipherKey))

print(encrypted_message)

decrypted_message = []
for ele in encrypted_message:
    decrypted_message.append(decrypt_chunk(ele,cipherKey))

print(decrypted_message)
