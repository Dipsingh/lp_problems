\* 3Node_MultiCommodity_MinCost_Routing *\
Minimize
OBJ: 2 x12 + x123 + 2 x13 + x132 + x213 + 2 x23
Subject To
_C1: x12 + x132 = 5
_C2: x123 + x13 = 10
_C3: x213 + x23 = 7
_C4: x12 + x123 + x213 <= 10
_C5: x13 + x132 + x213 <= 10
_C6: x123 + x132 + x23 <= 15
Bounds
0 <= x12 <= 10
0 <= x123 <= 10
0 <= x13 <= 10
0 <= x132 <= 10
0 <= x213 <= 10
0 <= x23 <= 10
Generals
x12
x123
x13
x132
x213
x23
End
