# Active-Absorbing Phase Transitions in the Parallel Minority Game

This repository contains the simulation code for the paper:

**"Active-Absorbing Phase Transitions in the Parallel Minority Game"**  
by Aryan Tyagi, Soumyajyoti Biswas, and Anirban Chakraborti

arXiv preprint: [arXiv:2512.22826](https://arxiv.org/abs/2512.22826)

## Overview

The Parallel Minority Game (PMG) is a synchronous adaptive multi-agent model exhibiting active-absorbing transitions characteristic of non-equilibrium statistical systems. This repository provides implementations of two distinct decision strategies:

### Decision Rules

**Instantaneous Strategy:**
```
p = (n_current - n_alternate) / (2 * n_current)
```
Agent switches with probability p when current site is more crowded than the alternative.

**Threshold Strategy:**
```
p = (n_current - g) / (2 * n_current)
```
Agent switches only when current site population exceeds the global average g, with probability based on the excess.

## Repository Structure

```
.
├── 1_ran2_generator.py          # Random number generator (Numerical Recipes)
├── 2_instantaneous_strategy.py  # Simulation with instantaneous decision rule
├── 3_threshold_strategy.py      # Simulation with threshold decision rule
└── README.md                    # This file
```

## Random Number Generator

The code uses the `ran2` algorithm from Numerical Recipes, a high-quality combined linear congruential generator with period > 2×10^18. This ensures reproducible results with controlled randomness.

### Parameters

Key simulation parameters (can be modified in the respective files):

- `D = 500`: Number of sites/locations
- `NRUN = 1500`: Number of independent runs for averaging
- `TMAX = 10000`: Number of time steps
- `G_VALUES`: Array of control parameter values spanning the critical point gc = 1

## Citation

```bibtex
@article{tyagi2025active,
  title={Active-Absorbing Phase Transitions in the Parallel Minority Game},
  author={Tyagi, Aryan and Biswas, Soumyajyoti and Chakraborti, Anirban},
  journal={arXiv preprint arXiv:2512.22826},
  year={2025}
}
```

## Contact

For questions or issues, please contact:
- Anirban Chakraborti: anirban@jnu.ac.in

## Acknowledgments

This work was conducted at:
- School of Computational & Integrative Sciences, Jawaharlal Nehru University, New Delhi
- Department of Physics, SRM University - AP, Andhra Pradesh

## References

The Parallel Minority Game framework and related studies:
- Biswas & Mandal (2021). Physica A 561, 125271
- Vemula & Biswas (2025). arXiv:2509.02770
