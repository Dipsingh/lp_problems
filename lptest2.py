import pulp


def main():
    demand = 20
    capacity = 10
    c12 = 1
    c132 = 2

    prob = pulp.LpProblem("3 Node Single Commodity Flow", pulp.LpMinimize)

    x12 = pulp.LpVariable('x12', lowBound=0, upBound=capacity, cat='Integer')
    x132 = pulp.LpVariable('x132', lowBound=0, upBound=capacity, cat='Integer')

    prob += (c12*x12+c132*x132)
    prob += (x12+x132 == demand)

    print(prob)

    prob.writeLP("3node SCF_SPF")

    # solve the LP using the default solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x12, x132):
        print('Optimal weekly number of {} to produce: {:1.0f}'.format(var.name, var.value()))


if __name__ == "__main__":
    main()