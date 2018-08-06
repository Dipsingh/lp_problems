\* 4 Node SCF *\
Minimize
OBJ: z
Subject To
_C1: x11 + x12 = 60
_C2: - x11 + 10 z >= 0
_C3: - x12 + 100 z >= 0
Bounds
0 <= x11 <= 10
0 <= x12 <= 100
Generals
x11
x12
End
