import pulp
import math


def min_cost_routing():
    c12, c13, c23 = 1,1,1
    c132, c123, c213 = 2,2,2

    h12 = 5
    h13 = 10
    h23 = 7

    cap12 = 10
    cap13 = 10
    cap23 = 15

    prob = pulp.LpProblem("3Node_MultiCommodity_MinCost_Routing", pulp.LpMinimize)

    # Defining the Flow Variables
    x12 = pulp.LpVariable('x12', lowBound=0, cat='Continuous')
    x132 = pulp.LpVariable('x132', lowBound=0, cat='Continuous')

    x13 = pulp.LpVariable('x13', lowBound=0, cat='Continuous')
    x123 = pulp.LpVariable('x123', lowBound=0, cat='Continuous')

    x23 = pulp.LpVariable('x23', lowBound=0, cat='Continuous')
    x213 = pulp.LpVariable('x213', lowBound=0, cat='Continuous')

    # Adding Objective Function
    prob += (c12 * x12 + c132 * x132 + c13 * x13 + c123 * x123 + c23 * x23 + c213 * x213)

    # Subject to Constraints
    prob += (x12 + x132 == h12)
    prob += (x13 + x123 == h13)
    prob += (x23 + x213 == h23)

    prob += (x12 + x123 + x213 <= cap12)
    prob += (x13 + x132 + x213 <= cap13)
    prob += (x23 + x132 + x123 <= cap23)

    # Print the Problem
    print(prob)

    prob.writeLP("3node_MCF_MinCost.lp")

    # solve the LP using the CPLEX Solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x12, x132, x13, x123, x23, x213):
        print('Optimal Flow for {} is {:1.0f}'.format(var.name, var.value()))

def min_cost_routing_diff_cost():
    c12, c13, c23 = 2,2,2
    c132, c123, c213 = 1,1,1

    h12 = 5
    h13 = 10
    h23 = 7

    cap12 = 10
    cap13 = 10
    cap23 = 15

    prob = pulp.LpProblem("3Node_MultiCommodity_MinCost_Routing", pulp.LpMinimize)

    # Defining the Flow Variables
    x12 = pulp.LpVariable('x12', lowBound=0, upBound=10, cat='Integer')
    x132 = pulp.LpVariable('x132', lowBound=0, upBound=10, cat='Integer')

    x13 = pulp.LpVariable('x13', lowBound=0, upBound=10, cat='Integer')
    x123 = pulp.LpVariable('x123', lowBound=0, upBound=10, cat='Integer')

    x23 = pulp.LpVariable('x23', lowBound=0, upBound=10, cat='Integer')
    x213 = pulp.LpVariable('x213', lowBound=0, upBound=10, cat='Integer')

    # Adding Objective Function
    prob += (c12 * x12 + c132 * x132 + c13 * x13 + c123 * x123 + c23 * x23 + c213 * x213)

    # Subject to Constraints
    prob += (x12 + x132 == h12)
    prob += (x13 + x123 == h13)
    prob += (x23 + x213 == h23)

    prob += (x12 + x123 + x213 <= cap12)
    prob += (x13 + x132 + x213 <= cap13)
    prob += (x23 + x132 + x123 <= cap23)

    # Print the Problem
    print(prob)

    prob.writeLP("3node_MCF_MinCost.lp")

    # solve the LP using the CPLEX Solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (x12, x132, x13, x123, x23, x213):
        print('Optimal Flow for {} is {:1.0f}'.format(var.name, var.value()))


def main():
    #min_cost_routing()
    min_cost_routing_diff_cost()


if __name__ == "__main__":
    main()
