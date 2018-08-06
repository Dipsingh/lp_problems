import pulp

def main():
    demand = 110
    capacity = 10

    prob = pulp.LpProblem("3 Node Single Commodity Flow", pulp.LpMinimize)

    x12 = pulp.LpVariable('x12', lowBound=0, upBound=capacity, cat='Integer')
    x132 = pulp.LpVariable('x132', lowBound=0, upBound=(10*capacity), cat='Integer')
    z = pulp.LpVariable('z', lowBound=0)

    prob += (z)
    prob += (x12+x132 == demand)
    prob += (z * capacity >= x12)
    prob += (z * 10 *capacity >= x132)

    print(prob)

    prob.writeLP("3node SCF_Loadbalancing")

    # solve the LP using the default solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x12, x132):
        print('Optimal number of {} to produce: {:1.0f}'.format(var.name, var.value()))


if __name__ == "__main__":
    main()