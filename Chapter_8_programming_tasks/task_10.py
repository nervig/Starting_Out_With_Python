
test_string = input("Enter an any text: ")
count = 0
# alfabet = "AEIOUBCDFGHJKLMNPQRSTVWXYZ"
a = 0
e = 0
i = 0
o = 0
u = 0
b = 0
c = 0
d = 0
f = 0
g = 0
h = 0
j = 0
k = 0
l = 0
m = 0
n = 0
p = 0
q = 0
r = 0
s = 0
t = 0
v = 0
w = 0
x = 0
y = 0
z = 0

for letter in test_string:
    if letter.lower() == 'a':
        a += 1
        if count < a:
            count = a
            name = 'a'
    if letter.lower() == 'e':
        e += 1
        if count < e:
            count = e
            name = 'e'
    if letter.lower() == 'i':
        i += 1
        if count < i:
            count = i
            name = 'i'
    if letter.lower() == 'o':
        o += 1
        if count < e:
            count = e
            name = 'e'
    if letter.lower() == 'u':
        u += 1
        if count < u:
            count = u
            name = 'u'
    if letter.lower() == 'b':
        b += 1
        if count < b:
            count = b
            name = 'b'
    if letter.lower() == 'c':
        c += 1
        if count < c:
            count = c
            name = 'c'
    if letter.lower() == 'd':
        d += 1
        if count < d:
            count = d
            name = 'd'
    if letter.lower() == 'f':
        f += 1
        if count < f:
            count = f
            name = 'f'
    if letter.lower() == 'g':
        g += 1
        if count < g:
            count = g
            name = 'g'
    if letter.lower() == 'h':
        h += 1
        if count < h:
            count = h
            name = 'h'
    if letter.lower() == 'j':
        j += 1
        if count < j:
            count = j
            name = 'j'
    if letter.lower() == 'k':
        k += 1
        if count < k:
            count = k
            name = 'k'
    if letter.lower() == 'l':
        l += 1
        if count < l:
            count = l
            name = 'l'
    if letter.lower() == 'm':
        m += 1
        if count < m:
            count = m
            name = 'm'
    if letter.lower() == 'n':
        n += 1
        if count < n:
            count = n
            name = 'n'
    if letter.lower() == 'p':
        p += 1
        if count < p:
            count = p
            name = 'p'
    if letter.lower() == 'q':
        q += 1
        if count < q:
            count = q
            name = 'q'
    if letter.lower() == 'r':
        r += 1
        if count < r:
            count = r
            name = 'r'
    if letter.lower() == 's':
        s += 1
        if count < s:
            count = s
            name = 's'
    if letter.lower() == 't':
        t += 1
        if count < t:
            count = t
            name = 't'
    if letter.lower() == 'v':
        v += 1
        if count < v:
            count = v
            name = 'v'
    if letter.lower() == 'w':
        w += 1
        if count < w:
            count = w
            name = 'w'
    if letter.lower() == 'x':
        x += 1
        if count < x:
            count = x
            name = 'x'
    if letter.lower() == 'y':
        y += 1
        if count < y:
            count = y
            name = 'y'
    if letter.lower() == 'z':
        z += 1
        if count < z:
            count = z
            name = 'z'

print(name)
print(count)
