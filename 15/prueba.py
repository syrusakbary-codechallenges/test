from bisect import bisect_left, bisect_right

# He creado la clase SuperRectangles que gestiona de la manera mas eficiente el problema,
# con coste (2*N+1)^2 siendo N el numero de rectangulos y no H*W que sería la manera más sencilla
# pero más ineficiente si H y W son ciertamente grandes
# Lo que hace el algoritmo es partir el canvas en 'cuadraditos' para después gestionar fácilmente sus colores.
class SuperRectangles:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.x = [0,width]
        self.y = [0,height]
        self.colors = {(width,height):1}
    def color_size (self):
        colors = {}
        for i in xrange(1,len(self.x)):
            act_x = self.x[i]
            for j in xrange(1,len(self.y)):
                act_y = self.y[j]
                color = self.colors[(act_x,act_y)]
                x = self.x[i-1]
                y = self.y[j-1]
                colors[color] = colors.get(color,0)+(act_y-y)*(act_x-x)
        return colors
    def format (self,n,m):
        return max(0,min(m,n))
    def insert (self,x1,x2,y1,y2,color):
        x1,x2,y1,y2 = self.format(x1,self.width),self.format(x2,self.width),self.format(y1,self.height),self.format(y2,self.height)
        a1 = bisect_right(self.x,x1)
        a2 = bisect_right(self.x,x2)
        insert_x1 = x1!=self.x[a1-1]
        insert_x2 = x2!=self.x[a2-1]
        b1 = bisect_right(self.y,y1)
        b2 = bisect_right(self.y,y2)
        insert_y1 = y1!=self.y[b1-1]
        insert_y2 = y2!=self.y[b2-1]
        colors = self.colors.copy()
        for i in self.x[1:]:
            if insert_y1: colors[(i,y1)] = self.colors[(i,self.y[b1])]
            if insert_y2: colors[(i,y2)] = self.colors[(i,self.y[b2])]
        for j in self.y[1:]:
            if insert_x1: colors[(x1,j)] = self.colors[(self.x[a1],j)]
            if insert_x2: colors[(x2,j)] = self.colors[(self.x[a2],j)]
        if insert_x1 and insert_y1: colors[(x1,y1)] = self.colors[(self.x[a1],self.y[b1])]
        if insert_x1 and insert_y2: colors[(x1,y2)] = self.colors[(self.x[a1],self.y[b2])]
        if insert_x2 and insert_y1: colors[(x2,y1)] = self.colors[(self.x[a2],self.y[b1])]
        if insert_x2 and insert_y2: colors[(x2,y2)] = self.colors[(self.x[a2],self.y[b2])]
        if insert_x1: self.x.insert(a1,x1)
        if insert_x2: self.x.insert(a2+(1 if insert_x1 else 0),x2)
        if insert_y1: self.y.insert(b1,y1)
        if insert_y2: self.y.insert(b2+(1 if insert_y1 else 0),y2)
        for i in self.x[1:]:
            for j in self.y[1:]:
                if x1<i<=x2 and y1<j<=y2:
                    colors[(i,j)] = color
        self.colors = colors

sr = SuperRectangles(15,100000000)
sr.insert(1,14,1,9,2)
print sr.color_size()
sr.insert(4,8,4,9,3)
print sr.color_size()
sr.insert(6,13,0,7,4)

d= sr.color_size()
exit()
divisions_x = [0,4,6,10]
divisions_y = [0,4,6,10]

#colors = {(10,10):1}
colors = {(4, 10): 1, (10, 6): 1, (6, 6): 10, (10, 4): 1, (10, 10): 1, (6, 10): 1, (4, 4): 1, (6, 4): 1, (4, 6): 1}
#insertar
#- Nueva linea divisions_x = [0,2,10] + ,(5,2):3,(7,2):3,(10,2):1
##Computar colores
c = {}
x = 0
y = 0
for i in xrange(1,len(divisions_x)):
    act_x = divisions_x[i]
    for j in xrange(1,len(divisions_y)):
        act_y = divisions_y[j]
        col = colors[(act_x,act_y)]
        x = divisions_x[i-1]
        y = divisions_y[j-1]
        c[col] = c.get(col,0)+(act_y-y)*(act_x-x)
print c


paint_color = 0

x1,x2 = 4,6
a1 = bisect_right(divisions_x,x1) # index del elemento mas proximo a 5 por la derecha
a2 = bisect_right(divisions_x,x2) # index del elemento mas proximo a 5 por la derecha

insert_x1 = x1!=divisions_x[a1-1]
insert_x2 = x2!=divisions_x[a2-1]
y1,y2 = 5,10
b1 = bisect_right(divisions_y,y1) # index del elemento mas proximo a 5 por la derecha
b2 = bisect_right(divisions_y,y2) # index del elemento mas proximo a 5 por la derecha


insert_y1 = y1!=divisions_y[b1-1]
insert_y2 = y2!=divisions_y[b2-1]


#for i in [divisions_x[a1],x1,x2]:
#    no_paint = i ==x1 or i==x2
#    for j in divisions_y[1:]:
#        if x1<i<=x2 and y1<j<=y2:
#            p = paint_color
#        else:
#            r1 = divisions_x[a2]
#            r2 = divisions_y[b2]
#            p = colors[(r1,r2)]
#        colors[(i,j)] = p
new_color = 11

new_colors = colors.copy()
print '* Antes'
print new_colors
for i in divisions_x[1:]:
    if insert_y1: new_colors[(i,y1)] = colors[(i,divisions_y[b1])]
    if insert_y2: new_colors[(i,y2)] = colors[(i,divisions_y[b2])]

for j in divisions_y[1:]:
    if insert_x1: new_colors[(x1,j)] = colors[(divisions_x[a1],j)]
    if insert_x2: new_colors[(x2,j)] = colors[(divisions_x[a2],j)]

print '* Bucle 1'
print new_colors

#new_colors[(5,7)] = 1
#new_colors[(5,5)] = 10
#new_colors[(7,5)] = 1
#colors[(x1,y1)] = colors[(divisions_x[a1],y1)]
#colors[(x1,y2)] = colors[(divisions_x[a1],y2)]
#colors[(x2,y1)] = colors[(x2,divisions_y[b1])]
#colors[(x2,y2)] = colors[(x2,divisions_y[b2])]
print 'Hola',(x2,y2),(divisions_x[a2-1],divisions_y[b2-1])
inc_x1 = 1 if insert_x1 else 0
inc_x2 = 1 if insert_x2 else 0
inc_y1 = 1 if insert_y1 else 0
inc_y2 = 1 if insert_y2 else 0

#new_colors[(x2,y1)] = colors[(divisions_x[a2],divisions_y[b1])]

if insert_x1 and insert_y1: new_colors[(x1,y1)] = colors[(divisions_x[a1],divisions_y[b1])]
if insert_x1 and insert_y2: new_colors[(x1,y2)] = colors[(divisions_x[a1],divisions_y[b2])]
if insert_x2 and insert_y1: new_colors[(x2,y1)] = colors[(divisions_x[a2],divisions_y[b1])]
if insert_x2 and insert_y2: new_colors[(x2,y2)] = colors[(divisions_x[a2],divisions_y[b2])]

#new_colors[(x1,y1)] = colors[(divisions_x[a1],divisions_y[b1])]
#new_colors[(x1,y2)] = colors[(divisions_x[a1],divisions_y[b2])]
#new_colors[(x2,y1)] = colors[(divisions_x[a2],divisions_y[b1])]
#new_colors[(x2,y2)] = colors[(divisions_x[a2],divisions_y[b2])]

print '* Despues asignacion'
print new_colors

if insert_x1: divisions_x.insert(a1,x1)
if insert_x2: divisions_x.insert(a2+inc_x1,x2)

#Anadir colores

    #for j in 
    #print divisions_x[i]
    
if insert_y1: divisions_y.insert(b1,y1)
if insert_y2: divisions_y.insert(b2+inc_y1,y2)

print divisions_x
print divisions_y

for i in divisions_x[1:]:
    for j in divisions_y[1:]:
        if x1<i<=x2 and y1<j<=y2:
            new_colors[(i,j)] = new_color
#for i in range(a1,a2):
#    for j in range(b1,b2):
#        new_colors[(divisions_x[i],divisions_y[j])] = new_color

#        elif (i!=x1 and i!=x2) and (j!=y1 and j!=y2):
#            new_colors[(i,j)] = colors[(i,j)]
print '* Final verif'
print new_colors

c = {}
x = 0
y = 0
for i in xrange(1,len(divisions_x)):
    act_x = divisions_x[i]
    for j in xrange(1,len(divisions_y)):
        act_y = divisions_y[j]
        col = new_colors[(act_x,act_y)]
        x = divisions_x[i-1]
        y = divisions_y[j-1]
        c[col] = c.get(col,0)+(act_y-y)*(act_x-x)
print c



