"""Analysis module for computing risk and infection rates."""


def infection_rate(outcomes: list[int]) -> float:
    """Calculate the infection rate from a list of outcomes."""
    if not outcomes:
        raise ValueError("Outcomes list must not be empty.")
    return sum(outcomes) / len(outcomes)


def relative_risk(control: list[int], treatment: list[int]) -> float:
    """Compute the relative risk between treatment and control groups."""
    control_rate = infection_rate(control)
    treatment_rate = infection_rate(treatment)

    if control_rate == 0:
        raise ZeroDivisionError("Control group infection rate is zero.")

    return treatment_rate / control_rate


def risk_reduction(control: list[int], treatment: list[int]) -> float:
    """Calculate the relative risk reduction."""
    return 1 - relative_risk(control, treatment)


def test_risk_reduction_no_effect() -> None:
    """Test risk reduction when treatment and control rates are equal."""
    control = [1, 0, 1]  # 2/3
    treatment = [1, 0, 1]  # 2/3
    assert risk_reduction(control, treatment) == 0.0  # 1 - 1.0
