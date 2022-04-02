
a = ['a', 'b', 'c']
b = ['1', '0', '0']
c = []
res = "\n".join("{} {} {}".format(x, y, z,) for x, y, z in zip(a, b, c))
print(res)