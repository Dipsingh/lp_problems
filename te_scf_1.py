import pulp

def main():
    demand = 60
    capacity = 10

    prob = pulp.LpProblem("4 Node SCF", pulp.LpMinimize)

    x11 = pulp.LpVariable('x11', lowBound=0, upBound=capacity, cat='Integer')
    x12 = pulp.LpVariable('x12', lowBound=0, upBound=10*capacity, cat='Integer')
    z = pulp.LpVariable('z', lowBound=0)

    prob += (z)
    prob += (x11+x12 == demand)
    prob += (z * capacity >= x11)
    prob += (z * 10* capacity >= x12)

    print(prob)

    prob.writeLP("4node_SCF_Loadbalancing.lp")

    # solve the LP using the CPLEX
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x11, x12):
        print('Optimal number of {} to produce: {:1.0f}'.format(var.name, var.value()))


if __name__ == "__main__":
    main()