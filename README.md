# CSDFS — Coupled Spectral Dynamical Field System

A distributed stochastic spectral dynamics framework for modeling, simulating, and analyzing metastable eigenmodes in high-dimensional neural systems.

---

## 🧠 Overview

CSDFS (Coupled Spectral Dynamical Field System) is a **distributed physics-inspired machine learning framework** that models high-dimensional intelligence systems as:

- Stochastic dynamical fields (Langevin dynamics)
- Coupled multi-node systems (Ray distributed actors)
- Spectral phase-space manifolds (eigenmode decomposition)

It enables:

- Detection of persistent latent sub-routines ("eigenmodes")
- Phase transition analysis of distributed AI systems
- Real-time interpretability of hidden-state dynamics
- Live visualization of cognitive phase-space evolution

---

## ⚙️ Core Idea

Each node evolves as:

\[
x_{t+1} = F(x_t) - \eta \nabla E(x_t) + \sqrt{2\eta T} \epsilon_t + \beta G(t) + \lambda \Pi_\perp
\]

Where:
- `E(x)` = learned neural energy field
- `β` = synchronization pressure (consensus)
- `λ` = orthogonal repulsion (diversity)
- `G(t)` = global mean field
- `ε_t` = stochastic noise

---

## 🚀 Features

- ⚡ Ray-distributed stochastic simulation engine
- 🧠 PyTorch-based neural energy fields
- 📊 Spectral eigenmode detection (real-time)
- 🌐 FastAPI + WebSocket live telemetry
- 🎨 React + D3 phase-space visualization dashboard
- 📄 Automated experiment + paper generation pipeline

---

## 📦 Installation

```bash
git clone git@github.com:ProjectLaunchPadLLC/csdfs.git
cd csdfs
pip install -e .
