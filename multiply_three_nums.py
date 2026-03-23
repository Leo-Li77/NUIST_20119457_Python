x = input("[Enter the first number]")
y = input("[Enter the second number]")
z = input("[Enter the third number]")

def mutipluy_three_nums(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    return (a * b *c)

print("[The result] <%0.2f>" % mutipluy_three_nums(x, y, z))
