\* 3Node_MultiCommodity_LoadBalancing *\
Minimize
OBJ: z
Subject To
_C1: x12 + x132 = 5
_C2: x123 + x13 = 10
_C3: x213 + x23 = 7
_C4: - x12 - x123 - x213 + 10 z >= 0
_C5: - x13 - x132 - x213 + 10 z >= 0
_C6: - x123 - x132 - x23 + 15 z >= 0
End
