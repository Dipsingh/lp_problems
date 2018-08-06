import numpy as np
import pulp
from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import seaborn as sns

def main():
    prob = pulp.LpProblem("test", pulp.LpMaximize)

#Variables
    soldiers = pulp.LpVariable('soliders', lowBound=0, cat='Integer')
    trains = pulp.LpVariable('trains', lowBound=0, cat='Integer')

#Objective Function
    raw_material_costs = 10 * soldiers + 9 * trains
    variable_costs = 14 * soldiers + 10 * trains
    revenues = 27 * soldiers+ 21 * trains

    profit = revenues - (raw_material_costs+ variable_costs)

    prob += profit


    # add constraints for available labor hours# add c
    carpentry_hours = soldiers + trains
    prob += (carpentry_hours <= 80)

    finishing_hours = 2*soldiers + trains
    prob += (finishing_hours <= 100)
    # add constraint representing demand for soldiers
    prob += (soldiers <= 40)

    print (prob)

    # solve the LP using the default solver
    optimization_result = prob.solve()

    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal

    # display the results
    for var in (soldiers, trains):
        print('Optimal weekly number of {} to produce: {:1.0f}'.format(var.name, var.value()))


    sns.set_color_palette('Set1')

    # create the plot object
    fig, ax = plt.subplots(figsize=(8, 8))
    s = np.linspace(0, 100)

    # add carpentry constraint: trains <= 80 - soldiers
    plt.plot(s, 80 - s, lw=3, label='carpentry')
    plt.fill_between(s, 0, 80 - s, alpha=0.1)

    # add finishing constraint: trains <= 100 - 2*soldiers
    plt.plot(s, 100 - 2 * s, lw=3, label='finishing')
    plt.fill_between(s, 0, 100 - 2 * s, alpha=0.1)

    # add demains constraint: soldiers <= 40
    plt.plot(40 * np.ones_like(s), s, lw=3, label='demand')
    plt.fill_betweenx(s, 0, 40, alpha=0.1)

    # add non-negativity constraints
    plt.plot(np.zeros_like(s), s, lw=3, label='t non-negative')
    plt.plot(s, np.zeros_like(s), lw=3, label='s non-negative')

    # highlight the feasible region
    path = Path([
        (0., 0.),
        (0., 80.),
        (20., 60.),
        (40., 20.),
        (40., 0.),
        (0., 0.),
    ])
    patch = PathPatch(path, label='feasible region', alpha=0.5)
    ax.add_patch(patch)

    # labels and stuff
    plt.xlabel('soldiers', fontsize=16)
    plt.ylabel('trains', fontsize=16)
    plt.xlim(-0.5, 100)
    plt.ylim(-0.5, 100)
    plt.legend(fontsize=14)
    plt.show()



if __name__ == "__main__":
    main()