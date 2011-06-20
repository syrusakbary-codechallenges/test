from PIL import Image
from bitarray import bitarray
i = "18/prueba.png"
img = Image.open(i)
rgbimg = img.convert('RGB')
w,h = img.size

all = bitarray()
def binary(n, digits=8):
    rep = bin(n)[2:]
    return ('0' * (digits - len(rep))) + rep

def bin2str(bin):
    bin2char = lambda s: chr(int(s,2))
    st = ""
    for i in range(0,len(bin),8):
        st += bin2char(bin[i:i+8])
    return (st)
import time
all=[]
for i in range(w):
    for j in range(h):
        d = rgbimg.getpixel((i, j))
        if d!=(0,255,0) and d!=(255,0,0):
            r,g,b = binary(d[0]), binary(d[1]), binary(d[2])
            all.append(r+g+b)

print bin2str(''.join(all))
