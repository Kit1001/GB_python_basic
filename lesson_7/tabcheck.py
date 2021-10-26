import os

a = r'1\2\3\check'
b = 'test'
c = os.path.join(a, b)
print(c)
d = os.path.split(c)
e = d[0]
g = os.path.split(e)
print(g)