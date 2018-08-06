import pulp


def main():
    prob = pulp.LpProblem("RSVP_TE_PathAllocation", pulp.LpMinimize)

    x_A_sf_kc = pulp.LpVariable('x_A_sf_kc', cat='Binary')
    x_A_sf_ny_kc = pulp.LpVariable('x_A_sf_ny_kc', cat='Binary')

    x_A_kc_ny = pulp.LpVariable('x_A_kc_ny', cat='Binary')
    x_A_kc_sf_ny = pulp.LpVariable('x_A_kc_sf_ny', cat='Binary')

    x_A_sf_ny = pulp.LpVariable('x_A_sf_ny', cat='Binary')
    x_A_sf_kc_ny = pulp.LpVariable('x_A_sf_kc_ny', cat='Binary')

    x_B_sf_ny = pulp.LpVariable('x_B_sf_ny', cat='Binary')
    x_B_sf_kc_ny = pulp.LpVariable('x_B_sf_kc_ny', cat='Binary')

    x_C_sf_ny = pulp.LpVariable('x_C_sf_ny', cat='Binary')
    x_C_sf_kc_ny = pulp.LpVariable('x_C_sf_kc_ny', cat='Binary')

    prob += (
        x_A_sf_kc + x_A_sf_ny_kc + x_A_kc_ny + x_A_kc_sf_ny + x_A_sf_ny +
        x_A_sf_kc_ny + x_B_sf_ny + x_B_sf_kc_ny + x_C_sf_ny + x_C_sf_kc_ny
    )

    prob += (x_A_sf_kc + x_A_sf_ny_kc == 1)
    prob += (x_A_kc_ny + x_A_kc_sf_ny == 1)
    prob += (x_A_sf_ny + x_A_sf_kc_ny == 1)
    prob += (x_B_sf_ny + x_B_sf_kc_ny == 1)
    prob += (x_C_sf_ny + x_C_sf_kc_ny == 1)

    prob += (45 * x_A_sf_kc + 60 * x_A_kc_sf_ny + 20 * x_A_sf_kc_ny + 80 * x_B_sf_kc_ny + 100 * x_C_sf_kc_ny <= 155)
    prob += (45 * x_A_sf_ny_kc + 60 * x_A_kc_sf_ny + 20 * x_A_sf_ny + 80 * x_B_sf_ny + 100 * x_C_sf_ny <= 155)
    prob += (45 * x_A_sf_ny_kc + 60 * x_A_kc_ny + 20 * x_A_sf_kc_ny + 80 * x_B_sf_kc_ny + 100 * x_C_sf_kc_ny <= 155)

    print(prob)

    prob.writeLP("RSVP_TE_PathAllocation.lp")

    # solve the LP using the CPLEX
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x_A_sf_kc, x_A_sf_ny_kc, x_A_kc_ny, x_A_kc_sf_ny, x_A_sf_ny, x_A_sf_kc_ny, x_B_sf_ny, x_B_sf_kc_ny,
                x_C_sf_ny, x_C_sf_kc_ny):
        print('Optimal number of {} to produce:{}'.format(var.name, var.varValue))


if __name__ == "__main__":
    main()
