import pulp
import math


def min_max_link_utilization():
    h12 = 5
    h13 = 10
    h23 = 7

    cap12 = 10
    cap13 = 10
    cap23 = 15

    prob = pulp.LpProblem("3Node_MultiCommodity_AvgDelay", pulp.LpMinimize)

    # Defining the Flow Variables
    x12 = pulp.LpVariable('x12', lowBound=0, cat='Continuous')
    x132 = pulp.LpVariable('x132', lowBound=0, cat='Continuous')

    x13 = pulp.LpVariable('x13', lowBound=0, cat='Continuous')
    x123 = pulp.LpVariable('x123', lowBound=0, cat='Continuous')

    x23 = pulp.LpVariable('x23', lowBound=0, cat='Continuous')
    x213 = pulp.LpVariable('x213', lowBound=0, cat='Continuous')

    y12 = pulp.LpVariable('y12', lowBound=0, cat='Continuous')
    y13 = pulp.LpVariable('y13', lowBound=0, cat='Continuous')
    y23 = pulp.LpVariable('y23', lowBound=0, cat='Continuous')

    z12 = pulp.LpVariable('z12', lowBound=0)
    z13 = pulp.LpVariable('z13', lowBound=0)
    z23 = pulp.LpVariable('z23', lowBound=0)

    # Adding Objective Function
    prob += (z12 * math.pow(cap12, -1) + z13 * math.pow(cap13, -1) + z23 * math.pow(cap23, -1))

    # Subject to Constraints
    prob += (x12 + x132 == h12)
    prob += (x13 + x123 == h13)
    prob += (x23 + x213 == h23)
    prob += (x12 + x123 + x213 == y12)
    prob += (x13 + x132 + x213 == y13)
    prob += (x23 + x123 + x123 == y23)

    prob += (z12 * 2 >= 3 * y12)
    prob += (z13 * 2 >= 3 * y13)
    prob += (z23 * 2 >= 3 * y23)

    prob += (z12 * 2 >= 9 * y12 - 2 * cap12)
    prob += (z13 * 2 >= 9 * y13 - 2 * cap13)
    prob += (z23 * 2 >= 9 * y23 - 2 * cap23)

    prob += (z12 >= 15 * y12 - 8 * cap12)
    prob += (z13 >= 15 * y13 - 8 * cap13)
    prob += (z23 >= 15 * y23 - 8 * cap23)

    prob += (z12 >= 50 * y12 - 36 * cap12)
    prob += (z13 >= 50 * y13 - 36 * cap13)
    prob += (z23 >= 50 * y23 - 36 * cap23)

    prob += (z12 >= 200 * y12 - 171 * cap12)
    prob += (z13 >= 200 * y13 - 171 * cap13)
    prob += (z23 >= 200 * y23 - 171 * cap23)

    prob += (z12 >= 4000 * y12 - 3781 * cap12)
    prob += (z13 >= 4000 * y13 - 3781 * cap13)
    prob += (z23 >= 4000 * y23 - 3781 * cap23)

    # Print the Problem
    print(prob)

    prob.writeLP("3node_MCF_AvgDelay.lp")

    # solve the LP using the CPLEX Solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x12, x132, x13, x123, x23, x213):
        print('Optimal Flow for {} is {:1.0f}'.format(var.name, var.value()))


def main():
    min_max_link_utilization()


if __name__ == "__main__":
    main()
