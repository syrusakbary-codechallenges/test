from pyDes import *
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from bitstring import *

#tuenti_bits = BitArray(b'0'*16+a[2:]).tostring()

# ECB, CBC
#f = open('19/file.bin')
def rest (byte1,byte2):
    return BitArray(int=byte1.int-byte2.int,length=byte1.len)
def decrypt(MODE,input):
    a = BitArray(bytes='tuenti')

    a.prepend('0b'+('0'*8))
    k = des("DESCRYPT",MODE, a.bytes)
    content = k.decrypt(input.bytes)
    return BitArray(bytes=content)
    
    
def decrypt2(cipher,input):
    from M2Crypto.EVP import Cipher
    encrypt = 0
    a = BitArray(bytes='tuenti')

    a.prepend('0b'+('0'*16))
    #a = rest(a,BitArray(int=1,length=a.len))
    cipher = Cipher(alg=cipher, key=a.bytes, op=encrypt, iv='\0'*16)
    ciphertext = cipher.update(input.bytes)
    ciphertext += cipher.final()
    return  BitArray(bytes=ciphertext)
def replace_xor(input):
    xor = BitArray(bytes='tuenti')
    r = BitArray()
    l = xor.len
    for i in range((input.len-xor.len)/8):
        p = i*8
        fin = p+xor.len
        r[p:fin] = (input[p:fin]^xor)
    return r

def replace_xor2(input):
    xor = BitArray(bytes='tuenti')
    r = BitArray(bytes=input.bytes)
    l = xor.len
    for i in range((input.len-xor.len)/8):
        p = i*8
        fin = p+xor.len
        r[p:fin] ^= xor
    return r
def replace_xor3(input):
    xor = BitArray(bytes='tuenti')
    xor.prepend('0b'+('0'*16))
    r = BitArray(bytes=input.bytes)
    l = xor.len
    for i in range((input.len-xor.len)/8):
        p = i*8
        fin = p+xor.len
        r[p:fin] = r[p:fin]^xor
    return r

def xor(input):
    m_cData = BitArray(bytes=input.bytes)
    #m_cKey = BitArray(bytes='tuenti')
    m_cKey = BitArray(bytes='tuenti')
    #m_cKey.prepend('0b'+('0'*16))
    
    keyPointer = 0
    keyPointerAdd = BitArray('0b00000000')

    for i in range(m_cData.len):
        keyPointerAdd = m_cData[i]
        m_cData[i] ^= m_cKey[keyPointer]
        keyPointer += keyPointerAdd
        #keyPointer += m_cData[i]
        keyPointer %= m_cKey.length
    return m_cData


def replace_xn(input):
    a = BitArray()
    for i in input.cut(8):
        a.append(rest(i,BitArray(int=1,length=8)))
    return a
    out = BitArray(bytes=input.bytes)
    #out = rest(out,BitArray(int=1,length=out.len))
    
    a = BitArray(hex='0x72')
    b = BitArray(hex='0x8D')
    #b = BitArray(uint=34,length=6)
    #a = BitArray(uint=29,length=6)

    #a = BitArray(bytes='\x34')
    #b = BitArray(bytes='\x29')
#out.replace(a,b)
    print '@@@@@@@@@@@@@@',out.replace(b,a)
    #for x in input.bytes:
    #    if ord(x)==114: x = chr(141)
    #    out.append(BitArray(bytes=x))
    return out

#f_contents = f.read()
import base64
f_contents = base64.decodestring('41qEb+UeY1nhNfTuUBQgltIFTeZEOh0BEC2CAKhu5TH8+ThABN+QD4jvIM2KcSJihrStv9D7rJiP90+5d0wlVDBikzxGci3AAp0SAwC/lONbxe2a+laGZPHU7YT3wt9MMOgL+p9V183/r+O7wAEmYgf02cyKY7jq4U/rg25orF8U7WGFCyjqegRl7SvePgEdtegywJbGrazBCriHaKwtLs/7yCfCWKVjQKC6m6TbOYydAz15rHWtcFOOHAh5sEtI8Ha5IL3Zv3RIx+HQaFCUFc1P+jNTrWUwmLBa2q61aY73qXM0Zx/ZUhixBraPOLeIOVFXrhc4Zo2Xqj/7W0XUSmxvi2wMzKNcUFvw+6qm0QM5T4ENSYRH7Q1Gv0uSEoBEhP/s2M/VGbz0pVNWDJjYBnNHBGY753MEjCrftzNiXfo=')

f2 = xor
f3 = replace_xn
f4 = lambda x:x

ciphers=[
            'des_ede_ecb', 'des_ede_cbc', 'des_ede_cfb', 'des_ede_ofb',
            'des_ede3_ecb', 'des_ede3_cbc', 'des_ede3_cfb', 'des_ede3_ofb',]
import time
for cipher in ciphers:
  try:
    print cipher
    i=BitArray(bytes=f_contents)
    i = decrypt2(cipher,i)
    i = replace_xn(i)
    i = xor(i)
    print i.bytes
    #for j in i.cut(8):
    #    print ord(j.bytes[0])
    time.sleep(1)
  except:pass
exit()
import itertools
for cipher in ciphers:
    f1 = lambda x: decrypt2(cipher,x)
    for funcs in itertools.permutations([f1,f2,f3]):
        try:
            i=BitArray(bytes=f_contents)
            a,b,c = funcs
            print a.__name__,b.__name__,c.__name__
            i = a(i)
            i = b(i)
            i = c(i)
            #i = d(i)
            #print i.bytes
            print  max([ord(x) for x in i.bytes])
        except:pass