from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import os


def pad(data_bytes):
    width = AES.block_size - len(data_bytes) % AES.block_size
    return data_bytes + bytes([width] * width)


def unpad(data_bytes):
    last_index = len(data_bytes) - 1
    last_byte = data_bytes[last_index]
    width = last_byte
    return data_bytes[:-width]


def aes_encrypt(key, iv, plain_bytes):
    aes = AES.new(key, AES.MODE_CBC, iv)
    padded_plain_bytes = pad(plain_bytes) 
    return aes.encrypt(padded_plain_bytes)


def aes_decrypt(key, iv, cipher_bytes):
    aes = AES.new(key, AES.MODE_CBC, iv)
    padded_plain_bytes = aes.decrypt(cipher_bytes)
    return unpad(padded_plain_bytes)

#เข้ารหัส
def aes_encrypt_file(key, iv, src_filename, dst_filename):
    with open(src_filename, 'rb') as fo:
        plain_bytes = fo.read()
    cipher_bytes = aes_encrypt(key, iv, plain_bytes)
    with open(dst_filename, 'wb') as fo:
        fo.write(cipher_bytes)

#ถอดรหัส
def aes_decrypt_file(key, iv, src_filename, dst_filename):
    with open(src_filename, 'rb') as fo:
        cipher_bytes = fo.read()
    plain_bytes = aes_decrypt(key, iv, cipher_bytes)
    with open(dst_filename, 'wb') as fo:
        fo.write(plain_bytes)

#แปลง bytes ให้เป็น str
def base64_encode_bytes_to_str(data_bytes):
    base64_bytes = b64encode(data_bytes)
    base64_ascii_str = base64_bytes.decode('ascii')
    return base64_ascii_str

#แปลง str ให้เป็น bytes
def base64_decode_str_to_bytes(base64_ascii_str):
    base64_bytes = base64_ascii_str.encode('ascii')
    data_bytes = b64decode(base64_bytes)
    return data_bytes

#สร้างและเขียน localkey
def save_local_key(aes_key, aes_iv, rsa_key, local_key_filename):
    pkcs1 = PKCS1_OAEP.new(rsa_key) #แปลง public key  
    aes_key_base64_str = base64_encode_bytes_to_str(aes_key)
    aes_iv_base64_str = base64_encode_bytes_to_str(aes_iv)
    local_key_base64_str = aes_key_base64_str + '\n' + aes_iv_base64_str
    local_key_base64_bytes = local_key_base64_str.encode('utf8')
    cipher_bytes = pkcs1.encrypt(local_key_base64_bytes) #เข้ารหัส AES+IV ด้วย pb key ที่แปลงมา
    with open(local_key_filename, 'wb') as fo: #สร้างไฟล์ localkey
        fo.write(cipher_bytes) #เขียน ASE+IV ลง localkey

#เปิดอ่าน localkey
def load_local_key(rsa_key, local_key_filename):
    pkcs1 = PKCS1_OAEP.new(rsa_key) #แปลง private key 
    with open(local_key_filename, 'rb') as fo: #เปิดไฟล์ localkey 
        cipher_bytes = fo.read() 
    local_key_base64_bytes = pkcs1.decrypt(cipher_bytes) #ถอดรหัส AES ด้วย pv key ที่แปลงมา
    local_key_base64_str = local_key_base64_bytes.decode('utf8')
    aes_key_base64_str, aes_iv_base64_str = local_key_base64_str.split('\n')
    aes_key = base64_decode_str_to_bytes(aes_key_base64_str)
    aes_iv = base64_decode_str_to_bytes(aes_iv_base64_str)
    return aes_key, aes_iv


rsa_public_key_str = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyIge8UVqxEy9FAzShyGP
WKoVcu6BlNVMyleceHc4+fwZG4cn9UxhPDwJ+LGCrCeRh8Qd7Pirlit66ZOTDTC8
8H7vbiwFpmJ3clonRA4BDQ/YSBtxJIPLJiMAZ5N7NIG25AyaBATznhLviWRZyfi0
ZSAsFbzNUm67ljb7jw4YDmv2UNx1tLt4VqpBNKTjANu1RrB9uPhQZhrXdkbxBPlj
AaP4E/XATdsgSru/o+ZUE9ABEwo4w18nc+G3rvePVrxFVoV2ISsaeJZnEpzBhsef
sDmedsvh+rnNZXH8NS1a0TyXpMHObzb5v3FwA4vYvO0M+LsQ8bxpSw50GCt3ZYtV
JwIDAQAB
-----END PUBLIC KEY-----
'''
rsa_public_key = RSA.import_key(rsa_public_key_str.strip())
default_local_key_filename = 'LocalKey'


def run_encryption_mode():
    aes_key = get_random_bytes(32) #random
    aes_iv = get_random_bytes(AES.block_size)  
    print('AES Key:', aes_key)
    src_filenames = ['sample.jpg', 'sample.txt'] #ไฟล์ที่ต้องการเข้ารหัส
    for src_filename in src_filenames:
        if os.path.exists(src_filename):
            dst_filename = src_filename + '.enc'
            aes_encrypt_file(aes_key, aes_iv, src_filename, dst_filename)
            print(f'The content of file {src_filename} has been encrypted into file {dst_filename}.')
            os.remove(src_filename)
            print(f'File {src_filename} has been removed.')
        else:
            print(f'File {src_filename} does not exist.')
    save_local_key(aes_key, aes_iv, rsa_public_key, default_local_key_filename) #เรียกใช้ฟังก์ชันที่สร้าง localkey
    print(f'AES Key and IV have been saved into file {default_local_key_filename}.')


def run_decryption_mode():
    print('Paste RSA Private Key and Press Enter:')
    rsa_private_key = input_rsa_private_key() #เก็บค่า input pv key
    aes_key, aes_iv = load_local_key(rsa_private_key, default_local_key_filename) #เรียกใช้ฟังก์ชันที่จะเปิดอ่าน localkey
    print('AES Key:', aes_key) 
    src_filenames = ['sample.jpg.enc', 'sample.txt.enc']
    for src_filename in src_filenames:
        if os.path.exists(src_filename):
            dst_filename = src_filename.rstrip('.enc')
            aes_decrypt_file(aes_key, aes_iv, src_filename, dst_filename)
            print(f'The content of file {src_filename} has been decrypted into file {dst_filename}.')
            os.remove(src_filename)
            print(f'File {src_filename} has been removed.')
        else:
            print(f'File {src_filename} does not exist.')

#input pv key
def input_rsa_private_key():
    rsa_private_key_str = ''
    while True:
        line = input()
        rsa_private_key_str += line + '\n'
        if line == '-----END RSA PRIVATE KEY-----':
            break
    return RSA.import_key(rsa_private_key_str.strip())


def main():
    print('Operation Modes')
    print('    1. Encryption Mode')
    print('    2. Decryption Mode')
    mode = int(input('Select an Operation Mode (Enter 1 or 2): '))
    if mode == 1:
        run_encryption_mode()
    elif mode == 2:
        run_decryption_mode()

#run main
if __name__ == '__main__':
    main()
