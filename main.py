#this file is for testing libraries, it is not included in the package
import PythonExtended.Math as m

t = m.triangleSolver()

t.a = 3
t.b = 5
t.C = 53.13

t.solve()
print(t.output)
print(t.a, t.b, t.c, t.A, t.B, t.C)

v = m.triangleSolver()

v.a = 12
v.c = 13
v.b = 5

v.solve()
print(v.output)
print(v.A, v.B, v.C)

