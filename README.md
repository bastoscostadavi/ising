# 2D Ising Model Monte Carlo Simulation

A comprehensive Python implementation of Monte Carlo simulations for the 2D Ising model using the Metropolis algorithm. This project includes finite size scaling analysis and visualization tools for studying phase transitions in statistical mechanics.

## Overview

The Ising model is a mathematical model used in statistical mechanics to describe ferromagnetism in statistical mechanics. This implementation simulates a 2D square lattice with periodic boundary conditions and calculates key thermodynamic properties including:

- **Energy per particle**
- **Magnetization per particle** 
- **Specific heat capacity**
- **Magnetic susceptibility**

## Features

- **Metropolis Algorithm**: Efficient implementation of the Metropolis-Hastings algorithm for Monte Carlo sampling
- **Periodic Boundary Conditions**: Uses cyclic boundary conditions implemented via extra lattice layers
- **Finite Size Scaling**: Analysis of critical behavior for different system sizes
- **Thermalization Studies**: Investigation of equilibration times
- **Data Visualization**: Comprehensive plotting tools for analysis
- **Multiple Data Sets**: Organized simulation results for different parameter sets

## Project Structure

```
├── README.md                 # This file
├── WARNING                   # Notes about data normalization
├── metropolis.py            # Core Metropolis algorithm implementation
├── simulation.py            # Main simulation runner
├── plot.py                  # Visualization and plotting tools
├── finite_size_scaling.py   # Finite size scaling analysis
├── termalization.py         # Thermalization time studies
├── data_organizer.py        # Data organization utilities
├── data/                    # Primary simulation results
├── data_set_1/             # First set of simulation data
├── data_set_2/             # Second set of simulation data  
├── data_set_3/             # Third set of simulation data
├── data_set_4/             # Fourth set of simulation data
└── figures/                # Generated plots and visualizations
```

## Core Algorithm

The simulation uses the Metropolis algorithm with the following key features:

### Energy Calculation
The energy change for flipping a spin is calculated as:
```
ΔE = 2J * s_k * Σ(s_neighbors)
```
where `s_k` is the spin to flip and the sum is over nearest neighbors.

### Acceptance Criterion
Spin flips are accepted with probability:
```
P = min(1, exp(-β * ΔE))
```
where `β = 1/(k_B * T)` is the inverse temperature.

### Boundary Conditions
Periodic boundary conditions are implemented using extra layers around the main lattice, allowing efficient neighbor calculations without explicit modular arithmetic.

## Usage

### Basic Simulation
```python
from metropolis import ising
import numpy as np

# Initialize lattice (20x20 with boundary layers)
l = 20
lattice = np.ones([l+2, l+2])

# Run simulation
beta = 1/2.5  # Inverse temperature
N = 1000000   # Monte Carlo steps
t = 250000    # Thermalization time

energy, magnetization, specific_heat, susceptibility, final_lattice, E_series, M_series = ising(beta, N, t, lattice)
```

### Running Simulations for Multiple System Sizes
```bash
python simulation.py
```

### Finite Size Scaling Analysis
```bash
python finite_size_scaling.py [property_name]
# property_name: energy, magnetization, heat, or susceptibility
```

### Plotting Results
```bash
python plot.py
```

## Key Parameters

- **l**: Linear system size (creates l×l lattice)
- **N**: Number of Monte Carlo steps
- **t**: Thermalization time (steps to discard for equilibration)
- **β**: Inverse temperature (1/k_B T)
- **Temperature range**: Typically 0.2 to 8.0 for comprehensive analysis

## Critical Temperature

The theoretical critical temperature for the 2D Ising model is:
```
T_c = 2J/(k_B * ln(1 + √2)) ≈ 2.269 J/k_B
```

This implementation uses J = k_B = 1, so T_c ≈ 2.269.

## Data Organization

### Data File Naming Convention
```
[property]_l[size]_N[steps]_t[thermalization].txt
```

Example: `energy_l10_N1000000_t250000.txt`

### Data Normalization Notes
**Important**: Different data sets use different normalization conventions (see `WARNING` file):

- **l = {15,20,25}**: Per particle quantities
- **l = {30,35,40}**: Total quantities (need division by N for per-particle values)

## Finite Size Scaling

The implementation includes finite size scaling analysis using:

- **Reduced temperature**: t = (T - T_c)/T_c
- **Scaling variables**: t × L for temperature scaling
- **Critical exponents**: 
  - Magnetization: β = 1/8
  - Susceptibility: γ = 7/4

## Visualization Features

The project generates various plots including:

- Energy vs temperature curves
- Magnetization phase transition
- Specific heat peaks near T_c
- Magnetic susceptibility divergence
- Finite size scaling functions
- Thermalization visualization

## Dependencies

```python
import numpy as np
import matplotlib.pyplot as plt
import ast
import sys
```

## Results

The simulation produces several key outputs:

1. **Phase Transition**: Clear ferromagnetic-paramagnetic transition around T_c ≈ 2.269
2. **Critical Behavior**: Diverging susceptibility and specific heat at the critical point
3. **Finite Size Effects**: Systematic study of how critical behavior depends on system size
4. **Scaling Functions**: Verification of finite size scaling theory

## Performance Notes

- Typical simulation: 1M Monte Carlo steps with 250k thermalization steps
- System sizes: 5×5 to 30×30 lattices
- Runtime scales as O(N × L²) where N is steps and L is linear size

## Scientific Applications

This implementation is suitable for:

- Statistical mechanics education
- Phase transition studies
- Critical phenomena research
- Monte Carlo method demonstration
- Finite size scaling investigations

## References

- Ising, E. (1925). "Beitrag zur Theorie des Ferromagnetismus"
- Metropolis, N. et al. (1953). "Equation of State Calculations by Fast Computing Machines"
- Onsager, L. (1944). "Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition"

## License

This project is open source and available under standard academic use terms.