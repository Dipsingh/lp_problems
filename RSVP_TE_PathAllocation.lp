\* RSVP_TE_PathAllocation *\
Minimize
OBJ: x_A_kc_ny + x_A_kc_sf_ny + x_A_sf_kc + x_A_sf_kc_ny + x_A_sf_ny
 + x_A_sf_ny_kc + x_B_sf_kc_ny + x_B_sf_ny + x_C_sf_kc_ny + x_C_sf_ny
Subject To
_C1: x_A_sf_kc + x_A_sf_ny_kc = 1
_C2: x_A_kc_ny + x_A_kc_sf_ny = 1
_C3: x_A_sf_kc_ny + x_A_sf_ny = 1
_C4: x_B_sf_kc_ny + x_B_sf_ny = 1
_C5: x_C_sf_kc_ny + x_C_sf_ny = 1
_C6: 60 x_A_kc_sf_ny + 45 x_A_sf_kc + 20 x_A_sf_kc_ny + 80 x_B_sf_kc_ny
 + 100 x_C_sf_kc_ny <= 155
_C7: 60 x_A_kc_sf_ny + 20 x_A_sf_ny + 45 x_A_sf_ny_kc + 80 x_B_sf_ny
 + 100 x_C_sf_ny <= 155
_C8: 60 x_A_kc_ny + 20 x_A_sf_kc_ny + 45 x_A_sf_ny_kc + 80 x_B_sf_kc_ny
 + 100 x_C_sf_kc_ny <= 155
Binaries
x_A_kc_ny
x_A_kc_sf_ny
x_A_sf_kc
x_A_sf_kc_ny
x_A_sf_ny
x_A_sf_ny_kc
x_B_sf_kc_ny
x_B_sf_ny
x_C_sf_kc_ny
x_C_sf_ny
End
