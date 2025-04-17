# Vaccine Trial Simulator

**Team Members**: Ailina Aniwan, Jay Liu

## Project Overview

This Python-based application simulates randomized vaccine trials with configurable parameters such as vaccine efficacy, population exposure rate, and group size. It computes key summary statistics including infection rates and relative infection risk reduction, and is designed as a modular, testable package with a simple command-line interface.

This project is developed as part of the final project for Biostat 821.


## General Software Architecture

- `src/vaxsim/`
    - `simulation.py`: Functions to simulate trial outcomes based on efficacy, exposure, and risk.
    - `analysis.py`: Functions to compute relative risk, infection rates, and summary statistics.
    - `cli.py`: (optional) Command-line interface for running and configuring trial simulations.
    - `models.py`: (optional) Data classes such as TrialGroup or PatientGroup to structure input/output.

- `tests/`: Unit tests covering simulation and analysis logic.
    - `test_simulation.py`: Unit tests for simulation logic.
    - `test_analysis.py`: Unit tests for statistical analysis functions.
    - `fake_trial_data.py`: (optional) Sample input data or fixtures used in testing.

- `.github/workflows/checks.yml`: GitHub Actions workflow for ruff, mypy, and pytest.
- `README.md`: Project overview, setup guide, usage examples, and contribution instructions.
- `pyproject.toml`: Project configuration file for dependency management and tool settings.
- `requirements-test.txt`: List of testing-related dependencies for development setup.
