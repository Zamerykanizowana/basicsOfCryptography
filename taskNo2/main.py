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

def xor_chunks(ch1, ch2):
    return bytes(a ^ b for a, b in zip(ch1,ch2))

# message to test
message_to_encrypt = b'I just want to finish this task and go to bed.'
# key
cipherKey = b'oskm3ucjakops2LA'
print(f'length mes: {len(message_to_encrypt)}')
pad_message = pad(message_to_encrypt,16)
print(f'length of pad_message: {len(pad_message)}')
print(f'pad_message: {pad_message}')

pad_message_in_chunks = chunk(pad_message, 16)
print(f'pad_message_in_chunks: {pad_message_in_chunks}')

# ECB
encrypted_message = []
for ele in pad_message_in_chunks:
    encrypted_message.append(encrypt_chunk(ele,cipherKey))
print(encrypted_message)

decrypted_message = []
for ele in encrypted_message:
    decrypted_message.append(decrypt_chunk(ele,cipherKey))
print(decrypted_message)

# CBC
encrypted_message = []
initialization_vector = b'ajsujnghkopkjasv'
for ele in pad_message_in_chunks:
    if len(encrypted_message) == 0:
        encrypted_message.append(encrypt_chunk(xor_chunks(ele,initialization_vector),cipherKey))
    else:
        encrypted_message.append(encrypt_chunk(xor_chunks(ele,encrypted_message[-1]),cipherKey))
print(encrypted_message)

decrypted_message = []
for idx, ele in enumerate(encrypted_message):
    if len(decrypted_message) == 0:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),initialization_vector))
    else:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),encrypted_message[idx-1]))
print(decrypted_message)

# PCBC
encrypted_message = []
helper_tab = []
for ele in pad_message_in_chunks:
    if len(encrypted_message) == 0:
        encrypted_message.append(encrypt_chunk(xor_chunks(ele,initialization_vector),cipherKey))
    else: 
        encrypted_message.append(encrypt_chunk(xor_chunks(ele, helper_tab[-1]),cipherKey))
    helper_tab.append(xor_chunks(encrypted_message[-1],ele))
print(encrypted_message)

decrypted_message = []
helper_tab = []
for idx, ele in enumerate(encrypted_message):
    if len(decrypted_message) == 0:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),initialization_vector))
    else:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),helper_tab[-1]))
    helper_tab.append(xor_chunks(decrypted_message[-1],ele))
print(decrypted_message)










