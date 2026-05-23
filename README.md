### 🎬 [Access the Full 26-Video Supplementary Simulation Suite Here](https://github.com/ashilsp/oloid-symmetric-universe/releases/tag/v1.0.0)

# Replacing the Big Bang Singularity with the OCM-Bounce: An Oloid-Symmetric Bridge Resolution to the Hubble Tension and Axis of Evil

Official open-source code and data replication repository for the **Original Cosmological Manifold (OCM)** framework.

## Abstract
Standard cosmological frameworks struggle to fully reconcile the $5.5\sigma$ Hubble tension alongside large-scale Cosmic Microwave Background (CMB) anomalies like the "Axis of Evil." This project introduces an Oloid-symmetric manifold bridge framework that replaces the primordial Big Bang singularity with a smooth, non-singular OCM-Bounce. By modeling cosmic expansion via developable geometric coordinates, we present a self-consistent architecture that bridges early-universe precision data with late-universe local distance ladder observations.

## Primary Code Engines
This repository houses the formal mathematical validation engines supporting both the primary manuscript and its corresponding Supplementary Information appendices:

* **`hubble_gradient.py`**: Solves the $n=3$ volumetric flux scaling profile across the Oloid manifold to smoothly transition $H_0$ from $67.4$ to $73.0\text{ km s}^{-1}\text{Mpc}^{-1}$.
* **`coordinate_mapping.py`**: Executes the 3D non-linear embedding transformations mapping intrinsic developable facets directly into standard astronomical Galactic coordinates $(l, b)$.
* **`laniakea_vectors.py`**: Models the 3D laminar drainage velocity field ($\vec{v}_T$) under the influence of Manifold Viscosity ($\eta_m$), generating the $600\text{ km s}^{-1}$ Laniakea bulk flow without dark matter overdensities.
* **`cosmic_drum_resonance.py`**: Computes the 2D boundary wave equation on a developable membrane cavity, verifying the scale-invariant pulsar timing residual strain index ($\gamma \to 1.00$).

## Repository Structure
```text
├── LICENSE                      # MIT Open-Source Legal Matrix
├── README.md                    # Project Repository Homepage
├── hubble_gradient.py           # Engine 1: Metric Gradient Solver
├── coordinate_mapping.py        # Engine 2: 3D Coordinate Transformer
├── laniakea_vectors.py          # Engine 3: Bulk Kinematics Vector Map
└── cosmic_drum_resonance.py     # Engine 4: Bounded Spectral Profiler
