from misFunciones import factorial as fct


n = int(input("Entre valor de n "))
r = int(input("Entre valor de r "))
fn = fct(n)
fr = fct(r)
fnr = fct(n - r)
nc = fn // fr // fnr
print("n =", n, "  r =", r, "  Factorial de n =", fn, "  Factorial de r =", fr, "  Factorial de n −r =", fnr,"  Número de combinaciones =", nc)