import pulp
import math


def min_max_link_utilization():
    h12 = 5
    h13 = 10
    h23 = 7

    cap12 = 10
    cap13 = 10
    cap23 = 15

    prob = pulp.LpProblem("3Node_MultiCommodity_LoadBalancing", pulp.LpMinimize)

    # Defining the Flow Variables
    x12 = pulp.LpVariable('x12', lowBound=0, cat='Continuous')
    x132 = pulp.LpVariable('x132', lowBound=0, cat='Continuous')

    x13 = pulp.LpVariable('x13', lowBound=0, cat='Continuous')
    x123 = pulp.LpVariable('x123', lowBound=0, cat='Continuous')

    x23 = pulp.LpVariable('x23', lowBound=0, cat='Continuous')
    x213 = pulp.LpVariable('x213', lowBound=0, cat='Continuous')

    z = pulp.LpVariable('z', lowBound=0)

    # Adding Objective Function
    prob += (z)

    # Subject to Constraints
    prob += (x12 + x132 == h12)
    prob += (x13 + x123 == h13)
    prob += (x23 + x213 == h23)

    prob += (z * cap12 >= x12 + x123 + x213)
    prob += (z * cap13 >= x13 + x132 + x213)
    prob += (z * cap23 >= x23 + x132 + x123)

    # Print the Problem
    print(prob)

    prob.writeLP("3node_MCF_LoadBalancing.lp")

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
