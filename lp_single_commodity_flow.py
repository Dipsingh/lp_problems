import pulp
import math


def min_cost_routing(capacity, demand, c12=1, c132=2):
    prob = pulp.LpProblem("3Node_SingleCommodity_MinCost_Routing", pulp.LpMinimize)

    # Defining the Flow Variables
    x12 = pulp.LpVariable('x12', lowBound=0, upBound=capacity, cat='Continuous')
    x132 = pulp.LpVariable('x132', lowBound=0, upBound=capacity, cat='Continuous')

    # Adding Objective Function
    prob += (c12 * x12 + c132 * x132)

    # Subject to Constraints
    prob += (x12 + x132 == demand)

    # Print the Problem
    #print(prob)

    prob.writeLP("3node_SCF_MinCost.lp")

    # solve the LP using the CPLEX Solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    return x12, x132


def load_balancing(capacity, demand):
    prob = pulp.LpProblem("3Node_SingleCommodity_LoadBalancing", pulp.LpMinimize)

    # Defining the Flow Variables
    x12 = pulp.LpVariable('x12', lowBound=0, upBound=capacity, cat='Continuous')
    x132 = pulp.LpVariable('x132', lowBound=0, upBound=(capacity), cat='Continuous')

    # Defining the Objective Function Variable
    z = pulp.LpVariable('z', lowBound=0)

    # Objective Function
    prob += (z)

    # Subject to Constraints
    prob += (x12 + x132 == demand)
    prob += (z * capacity >= x12)
    prob += (z * capacity >= x132)

    # Print the Problem
    #print(prob)

    prob.writeLP("3node_SCF_LoadBalancing.lp")

    # solve the LP using the CPLEX Solver
    optimization_result = prob.solve(pulp.CPLEX())

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    return x12, x132


def average_delay(capacity, demand):
    x12 = -demand + (3 * capacity) - (2 * math.sqrt(2)) * capacity + (math.sqrt(2)) * demand

    return x12


def main():
    link_capacity = 10
    demand = 15

    min_cost_routing_x12 = list()
    for demand in range(20):
        x12, x132 = min_cost_routing(capacity=link_capacity, demand=demand)
        min_cost_routing_x12.append(x12.value())

    print ("Min Cost Routing Result ", min_cost_routing_x12)

    # # display the results
    # for var in (x12, x132):
    #     print('Optimal flows for MinCostRouting {}  {:1.0f}'.format(var.name, var.value()))

    load_balancing_x12 = list()
    for demand in range(20):
        x12, x132 = load_balancing(capacity=link_capacity, demand=demand)
        load_balancing_x12.append(x12.value())

    print ("LoadBalancing Redult", load_balancing_x12)

    # # display the results
    # for var in (x12, x132):
    #     print('Optimal flows for LoadBalancing {}  {:1.0f}'.format(var.name, var.value()))

    average_delay_x12 = list()
    for demand in range(20):
        x12 = average_delay(capacity=link_capacity, demand=10)
        average_delay_x12.append(x12)

    print ("Optimal Flows for Average Delay {}".format(average_delay_x12))

    



if __name__ == "__main__":
    main()
