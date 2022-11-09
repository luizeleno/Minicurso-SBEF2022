import functools

def f(x, y, z):
    return x + y + z

f12 = lambda x: f(x, 1, 2)
f12a = functools.partial(f, y=1, z=2)

print(f(1, 1, 2))
print(f12(1))
print(f12a(1))
