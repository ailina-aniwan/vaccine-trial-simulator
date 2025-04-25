"""Simulation module for vaccine trial outcomes."""

import random


def simulate_trial(
    group_size: int,
    exposure_rate: float,
    baseline_risk: float,
    vaccine_efficacy: float,
) -> tuple[list[int], list[int]]:
    """Simulate a randomized vaccine trial.

    Args:
        group_size (int): Number of individuals per group.
        exposure_rate (float): Probability of exposure to the disease.
        baseline_risk (float): Probability of infection if exposed and
            unvaccinated.
        vaccine_efficacy (float): Proportional reduction in infection risk.

    Returns:
        tuple[list[int], list[int]]: Infection outcomes for control and
            treatment groups. 1 = infected, 0 = not infected.
    """
    control_group = []
    treatment_group = []

    for _ in range(group_size):
        # Control group
        exposed = random.random() < exposure_rate
        infected = exposed and (random.random() < baseline_risk)
        control_group.append(int(infected))

        # Treatment group
        exposed = random.random() < exposure_rate
        adjusted_risk = baseline_risk * (1 - vaccine_efficacy)
        infected = exposed and (random.random() < adjusted_risk)
        treatment_group.append(int(infected))

    return control_group, treatment_group

