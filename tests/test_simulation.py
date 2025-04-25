"""Tests for the simulation module."""

import random
from typing import cast  # Add import for cast

import pytest

from vaxsim.simulation import simulate_trial


@pytest.fixture
def default_params() -> dict[str, float | int]:
    """Default parameters for simulation tests."""
    return {
        "group_size": 100,
        "exposure_rate": 0.5,
        "baseline_risk": 0.2,
        "vaccine_efficacy": 0.7,
    }


def test_simulate_trial_output_length(
    default_params: dict[str, float | int],
) -> None:
    """Test that simulate_trial returns correct output lengths."""
    group_size = cast(
        int, default_params["group_size"]
    )  # Assert group_size is int
    control, treatment = simulate_trial(
        group_size=group_size,
        exposure_rate=default_params["exposure_rate"],
        baseline_risk=default_params["baseline_risk"],
        vaccine_efficacy=default_params["vaccine_efficacy"],
    )
    assert len(control) == default_params["group_size"]
    assert len(treatment) == default_params["group_size"]


def test_simulate_trial_binary_outcomes(
    default_params: dict[str, float | int],
) -> None:
    """Test that outcomes are binary (0 or 1)."""
    group_size = cast(
        int, default_params["group_size"]
    )  # Assert group_size is int
    control, treatment = simulate_trial(
        group_size=group_size,
        exposure_rate=default_params["exposure_rate"],
        baseline_risk=default_params["baseline_risk"],
        vaccine_efficacy=default_params["vaccine_efficacy"],
    )
    assert all(outcome in [0, 1] for outcome in control)
    assert all(outcome in [0, 1] for outcome in treatment)


def test_simulate_trial_zero_efficacy(
    default_params: dict[str, float | int],
) -> None:
    """Test simulation with zero vaccine efficacy (control ≈ treatment)."""
    # Set a random seed for reproducibility
    random.seed(42)
    group_size = cast(
        int, default_params["group_size"]
    )  # Assert group_size is int
    control, treatment = simulate_trial(
        group_size=group_size,
        exposure_rate=default_params["exposure_rate"],
        baseline_risk=default_params["baseline_risk"],
        vaccine_efficacy=0.0,  # Override vaccine_efficacy
    )
    control_infections = sum(control)
    treatment_infections = sum(treatment)
    # With zero efficacy, expect similar infection counts
    # (within 20% of control infections due to randomness)
    assert (
        abs(control_infections - treatment_infections)
        < 0.2 * control_infections
    )


def test_simulate_trial_full_efficacy(
    default_params: dict[str, float | int],
) -> None:
    """Test simulation with 100% vaccine efficacy (no treatment infections)."""
    group_size = cast(
        int, default_params["group_size"]
    )  # Assert group_size is int
    control, treatment = simulate_trial(
        group_size=group_size,
        exposure_rate=default_params["exposure_rate"],
        baseline_risk=default_params["baseline_risk"],
        vaccine_efficacy=1.0,  # Override vaccine_efficacy
    )
    assert sum(treatment) == 0  # No infections in treatment group


def test_simulate_trial_zero_exposure(
    default_params: dict[str, float | int],
) -> None:
    """Test simulation with zero exposure rate (no infections)."""
    group_size = cast(
        int, default_params["group_size"]
    )  # Assert group_size is int
    control, treatment = simulate_trial(
        group_size=group_size,
        exposure_rate=0.0,  # Override exposure_rate
        baseline_risk=default_params["baseline_risk"],
        vaccine_efficacy=default_params["vaccine_efficacy"],
    )
    assert sum(control) == 0
    assert sum(treatment) == 0


def test_simulate_trial_zero_group_size() -> None:
    """Test simulation with zero group size."""
    control, treatment = simulate_trial(
        group_size=0,
        exposure_rate=0.5,
        baseline_risk=0.2,
        vaccine_efficacy=0.7,
    )
    assert control == []
    assert treatment == []


def test_simulate_trial_invalid_inputs() -> None:
    """Test simulation with invalid inputs."""
    with pytest.raises(ValueError, match="group_size must be non-negative"):
        simulate_trial(-1, 0.5, 0.2, 0.7)
    with pytest.raises(
        ValueError, match="exposure_rate must be between 0 and 1"
    ):
        simulate_trial(100, -0.1, 0.2, 0.7)
    with pytest.raises(
        ValueError, match="baseline_risk must be between 0 and 1"
    ):
        simulate_trial(100, 0.5, 1.1, 0.7)
    with pytest.raises(
        ValueError, match="vaccine_efficacy must be between 0 and 1"
    ):
        simulate_trial(100, 0.5, 0.2, -0.1)
