# Vaccine Trial Simulator

**Contributors**: Ailina Aniwan, Jay Liu

## Project Overview

This Python-based application simulates randomized vaccine trials with configurable parameters such as vaccine efficacy, population exposure rate, and group size. It computes key summary statistics including infection rates, relative risk, and relative risk reduction. The project is structured as a modular, testable Python package with full CI support.

This project is developed as part of the final project for Biostat 821.

## Installation & Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/ailina-aniwan/vaccine-trial-simulator
    cd vaccine-trial-simulator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements-test.txt
    ```

3. Example usage:
    ```python
    from vaxsim.simulation import simulate_trial
    from vaxsim.analysis import infection_rate, relative_risk, risk_reduction

    control, treatment = simulate_trial(100, 0.5, 0.2, 0.7)
    print("Control rate:", infection_rate(control))
    print("Treatment rate:", infection_rate(treatment))
    print("Relative risk:", relative_risk(control, treatment))
    print("Risk reduction:", risk_reduction(control, treatment))
    ```

## Project Structure

- `src/vaxsim/`
    - `simulation.py`: Functions to simulate trial outcomes based on efficacy, exposure, and risk.
    - `analysis.py`: Functions to compute relative risk, infection rates, and summary statistics.

- `tests/`: Unit tests covering simulation and analysis logic.
    - `test_simulation.py`: Unit tests for simulation logic.
    - `test_analysis.py`: Unit tests for statistical analysis functions.

- `.github/workflows/checks.yml`: GitHub Actions workflow for ruff, mypy, and pytest.
- `README.md`: Project overview, setup guide, usage examples, and contribution instructions.
- `pyproject.toml`: Project configuration file for dependency management and tool settings.
- `requirements-test.txt`: List of testing-related dependencies for development setup.

## Running Tests

- To run all tests locally:
    ```bash
    pytest
    ```

- To check style and types:
    ```bash
    ruff check .
    mypy .
    ```
CI will run these checks automatically on all pull requests.


## Developer Notes

- Python version: 3.11 (recommended)
- Follows PEP8 and strict type checking
- All functions include type hints and docstrings
- Uses Ruff, MyPy, and Pytest with GitHub Actions for CI