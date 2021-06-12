def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

n = int(input("Entre valor de n "))
r = int(input("Entre valor de r "))
fn = factorial(n)
fr = factorial(r)
fnr = factorial(n - r)
nc = fn// fr// fnr
print("n =", n, "  r =", r, "  Factorial de n =", fn, "  Factorial de r =", fr, "  Factorial de n −r =", fnr,"  Número de combinaciones =", nc)