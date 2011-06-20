from PIL import Image
from bitarray import bitarray
i = "17/program.png"
img = Image.open(i)
rgbimg = img.convert('RGB')
w,h = img.size
rev = [lambda x:x, lambda x: reversed(x)]
orders = ([0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,1,0],[2,0,1])
endians =  ['big','little']
notes = [0,1,2]
def bin2str(bin):
    bin2char = lambda s: chr(int(s,2))
    st = ""
    for i in range(0,len(bin),8):
        st += bin2char(bin[i:i+8])
    return (st)
import time
bits_r,bits_g,bits_b = [],[],[]
for j in range(h):
    for i in range(w):
        d = rgbimg.getpixel((i, j))
        r,g,b = d[0]&1, d[1]&1, d[2]&1
        r,g,b = str(r),str(g),str(b)
        bits_r.append(r)
        bits_g.append(g)
        bits_b.append(b)

def imerge(a,b,c=None):
    if c:
        for i,j,k in zip(a,b,c):
            yield i
            yield j
            yield k
    else:
        for i,j in zip(a,b):
            yield i
            yield j

total =  [
          imerge(bits_r,bits_g,bits_b),
          imerge(bits_r,bits_b,bits_g),
          imerge(bits_b,bits_r,bits_g),
          imerge(bits_b,bits_g,bits_r),
          imerge(bits_g,bits_r,bits_b),
          imerge(bits_g,bits_b,bits_r),
          bits_r+bits_g+bits_b,
          bits_r+bits_b+bits_g,
          bits_b+bits_r+bits_g,
          bits_b+bits_g+bits_r,
          bits_g+bits_r+bits_b,
          bits_g+bits_b+bits_r,
          ]

for l in total:
    bits = list(l)
    print '\n\n\n\n\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n\n\n\n\n\n',bin2str(''.join(bits))
    time.sleep(1)
