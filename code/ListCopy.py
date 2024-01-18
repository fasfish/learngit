a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a
b.append(20)
print(a)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c.append(20)
print(d)

e = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [] + e
e.append(20)
print(f)
