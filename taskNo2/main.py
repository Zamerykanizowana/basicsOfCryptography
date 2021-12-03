from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
from copy import deepcopy


def chunk(m, size):
    tab_res = []
    i = 0
    while i+size <= len(m):
        tab_res.append(m[i:i+size])
        i += size
    return tab_res

def unchunk(tab_m):
    return b''.join(tab_m)

def encrypt_chunk(m, k):
    return AES.new(key=k, mode=AES.MODE_ECB).encrypt(m)

def decrypt_chunk(m, k):
    return AES.new(key=k, mode=AES.MODE_ECB).decrypt(m)

def xor_chunks(ch1, ch2):
    return bytes(a ^ b for a, b in zip(ch1,ch2))

def test_ciper_encryption_decryption(en_m, de_m, mode):
    print(f'{mode}: ' + ('\x1b[32mmessage correct encrypted, decrypted\x1b[0m' if en_m == de_m else\
            '\x1b[31msomething gets wrong\x1b[0m'))

def all_tests(secret_message):
    def _remove_chunk(s_m,idx):
        sec_m = deepcopy(s_m)
        print(f'\x1b[33mtest line: sec_m: {sec_m}\x1b[0m')
        del sec_m[idx]
        return sec_m

    def _double_chunk(sec_m,idx):
        result = []
        for idx_s, ele in enumerate(sec_m):
            if idx_s == idx:
                result.append(ele)
            result.append(ele)
        return result

    def _swap_chunks(s_m,idx):
        sec_m = deepcopy(s_m)
        # swap with next chunk if possible, else with previous
        print(f'\x1b[33mtest line: idx: {idx} len(sec_m): {len(sec_m)}\x1b[0m')
        print(f'\x1b[33mtest line: sec_m: {sec_m}\x1b[0m')
        if idx == len(sec_m)-2:
            sec_m[idx], sec_m[idx+1] = sec_m[idx+1], sec_m[idx]
        else:
            sec_m[idx], sec_m[idx-1] = sec_m[idx-1], sec_m[idx]
        return sec_m

    def _change_byte_in_chunk(s_m, idx):
        sec_m = deepcopy(s_m)
        byte_idx_to_change = random.randint(0,len(sec_m[0])-1)
        print(f'all_tests: _change_byte_in_chunk: byte_idx_to_change: {byte_idx_to_change}')
        new_chunk = b''.join([b'\x00'*byte_idx_to_change, b'r', b'\x00'*(15-byte_idx_to_change)])
        sec_m[idx] = new_chunk
        return sec_m

    def _swap_bytes_in_chunk(s_m, idx):
        sec_m = deepcopy(s_m)
        sec_m[idx] = b''.join([sec_m[idx][8:],sec_m[idx][:8]])
        return sec_m

    def _remove_byte_in_chunk(s_m, idx):
        sec_m = deepcopy(s_m)
        sec_m[idx] = sec_m[idx][:-1]
        return sec_m

    #selected_chunk_idx = random.randint(0,len(secret_message)-1)
    selected_chunk_idx = 2 
    print(f'all_tests: random index to test: {selected_chunk_idx} from {len(secret_message)}')
    print(f'secret_message:\n')
    print(secret_message)
    print('-------------- tests ---------------')
    rem_ch_test = _remove_chunk(secret_message,selected_chunk_idx)
    dou_ch_test = _double_chunk(secret_message,selected_chunk_idx)
    swa_ch_test = _swap_chunks(secret_message,selected_chunk_idx)
    cha_b_test = _change_byte_in_chunk(secret_message,selected_chunk_idx)
    swa_b_test = _swap_bytes_in_chunk(secret_message,selected_chunk_idx)
    rem_b_test = _remove_byte_in_chunk(secret_message,selected_chunk_idx)
    print('_remove_chunk result:')
    print(rem_ch_test)
    print('_double_chunk result:')
    print(dou_ch_test)
    print('_swap_chunk result:')
    print(swa_ch_test)
    print('_change_byte_in_chunk result:')
    print(cha_b_test)
    print('_swap_byte_in_chunk result:')
    print(swa_b_test)
    print('_remove_byte_in_chunk result:')
    print(rem_b_test)

    
    
# message to test
message_to_encrypt = b'I just want to finish this task and go to bed.'
# key
cipherKey = b'oskm3ucjakops2LA'
print(f'length mes: {len(message_to_encrypt)}')
pad_message = pad(message_to_encrypt,16)
print(f'length of pad_message: {len(pad_message)}')
#print(f'pad_message: {pad_message}')
pad_message_in_chunks = chunk(pad_message, 16)
#print(f'pad_message_in_chunks: {pad_message_in_chunks}')

# ECB
encrypted_message = []
for ele in pad_message_in_chunks:
    encrypted_message.append(encrypt_chunk(ele,cipherKey))
print(f'encrypted_message:\n{encrypted_message}')

all_tests(encrypted_message)

decrypted_message = []
for ele in encrypted_message:
    decrypted_message.append(decrypt_chunk(ele,cipherKey))
test_ciper_encryption_decryption(message_to_encrypt, unpad(unchunk(decrypted_message),16),'ECB')

# CBC
encrypted_message = []
initialization_vector = b'ajsujnghkopkjasv'
for ele in pad_message_in_chunks:
    if len(encrypted_message) == 0:
        encrypted_message.append(encrypt_chunk(xor_chunks(ele,initialization_vector),cipherKey))
    else:
        encrypted_message.append(encrypt_chunk(xor_chunks(ele,encrypted_message[-1]),cipherKey))

decrypted_message = []
for idx, ele in enumerate(encrypted_message):
    if len(decrypted_message) == 0:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),initialization_vector))
    else:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),encrypted_message[idx-1]))
test_ciper_encryption_decryption(message_to_encrypt, unpad(unchunk(decrypted_message),16),'CBC')


# PCBC
encrypted_message = []
helper_tab = []
for ele in pad_message_in_chunks:
    if len(encrypted_message) == 0:
        encrypted_message.append(encrypt_chunk(xor_chunks(ele,initialization_vector),cipherKey))
    else: 
        encrypted_message.append(encrypt_chunk(xor_chunks(ele, helper_tab[-1]),cipherKey))
    helper_tab.append(xor_chunks(encrypted_message[-1],ele))

decrypted_message = []
helper_tab = []
for idx, ele in enumerate(encrypted_message):
    if len(decrypted_message) == 0:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),initialization_vector))
    else:
        decrypted_message.append(xor_chunks(decrypt_chunk(ele,cipherKey),helper_tab[-1]))
    helper_tab.append(xor_chunks(decrypted_message[-1],ele))
test_ciper_encryption_decryption(message_to_encrypt, unpad(unchunk(decrypted_message),16),'PCBC')









