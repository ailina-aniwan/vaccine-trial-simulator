"""Tests for the analysis module."""

import pytest

from vaxsim.analysis import infection_rate, relative_risk, risk_reduction


@pytest.fixture
def sample_outcomes() -> dict[str, list[int]]:
    """Sample outcomes for testing."""
    return {
        "control": [1, 0, 1, 0, 0],  # 2/5 infected
        "treatment": [0, 0, 1, 0, 0],  # 1/5 infected
    }


def test_infection_rate_basic(sample_outcomes: dict[str, list[int]]) -> None:
    """Test infection rate calculation."""
    assert infection_rate(sample_outcomes["control"]) == 0.4  # 2/5
    assert infection_rate(sample_outcomes["treatment"]) == 0.2  # 1/5


def test_infection_rate_empty_list() -> None:
    """Test infection rate with empty list."""
    with pytest.raises(ValueError, match="Outcomes list must not be empty"):
        infection_rate([])


def test_infection_rate_all_infected() -> None:
    """Test infection rate when all are infected."""
    assert infection_rate([1, 1, 1]) == 1.0


def test_infection_rate_none_infected() -> None:
    """Test infection rate when none are infected."""
    assert infection_rate([0, 0, 0]) == 0.0


def test_relative_risk_basic(sample_outcomes: dict[str, list[int]]) -> None:
    """Test relative risk calculation."""
    rr = relative_risk(
        sample_outcomes["control"], sample_outcomes["treatment"]
    )
    assert rr == 0.5  # treatment_rate (0.2) / control_rate (0.4)


def test_relative_risk_zero_control_rate() -> None:
    """Test relative risk with zero control rate."""
    control = [0, 0, 0]
    treatment = [1, 0, 0]
    with pytest.raises(
        ZeroDivisionError, match="Control group infection rate is zero"
    ):
        relative_risk(control, treatment)


def test_risk_reduction_basic(sample_outcomes: dict[str, list[int]]) -> None:
    """Test risk reduction calculation."""
    rrr = risk_reduction(
        sample_outcomes["control"], sample_outcomes["treatment"]
    )
    assert rrr == 0.5  # 1 - relative_risk (0.5)


def test_risk_reduction_zero_control_rate() -> None:
    """Test risk reduction with zero control rate."""
    control = [0, 0, 0]
    treatment = [1, 0, 0]
    with pytest.raises(
        ZeroDivisionError, match="Control group infection rate is zero"
    ):
        risk_reduction(control, treatment)


def test_risk_reduction_no_effect() -> None:
    """Test risk reduction when treatment and control rates are equal."""
    control = [1, 0, 1]  # 2/3
    treatment = [1, 0, 1]  # 2/3
    assert risk_reduction(control, treatment) == 0.0  # 1 - 1.0
