\* 3Node_SingleCommodity_LoadBalancing *\
Minimize
OBJ: z
Subject To
_C1: x12 + x132 = 19
_C2: - x12 + 10 z >= 0
_C3: - x132 + 10 z >= 0
Bounds
x12 <= 10
x132 <= 10
End
