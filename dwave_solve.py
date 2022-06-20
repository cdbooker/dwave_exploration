
import dimod
import numpy as np
from neal import SimulatedAnnealingSampler
from dwave.system import LeapHybridCQMSampler

def load_constrained_quadratic_model(filename):
    cqm = dimod.lp.load(filename)
    print(cqm.constraints)
    print(cqm.objective)
    print(cqm.variables)
    return cqm


def solve_constrained_quadratic_model(cqm):
    sampler = LeapHybridCQMSampler()
    sampleset = sampler.sample_cqm(cqm)
    feasible_samples = []
    feasible_energies = []
    for sample, E in sampleset.data(fields=['sample', 'energy']):
        # Check all solutions for feasibility
        if cqm.check_feasible(sample):
            feasible_samples.append(sample)
            feasible_energies.append(E)
    optimal_val = np.array(feasible_energies).min()
    optimal_sol = feasible_samples[np.array(feasible_energies).argmin()]
    info = sampleset.info
    return optimal_val, optimal_sol, info


if __name__ == '__main__':
    file = 'test_problem.lp'
    model = load_constrained_quadratic_model(file)

    optimal_value, optimal_solution, solver_info = solve_constrained_quadratic_model(model)
    print(optimal_value)
    print(optimal_solution)


