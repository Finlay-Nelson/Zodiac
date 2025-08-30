# Microscopy Assembly Platform

This repository contains software for controlling microscopy experiments,
running automated workflows, and processing experimental data.

## Features (planned)
- Hardware control (e.g., cameras, motors, illumination)
- Experiment orchestration
- Data analysis and visualization
- CLI for advanced users
- GUI for everyday lab users

## Installation
For developers:
```bash
git clone https://github.com/<YourUsername>/microscopy-assembly.git
cd microscopy-assembly
conda env create -f environment.yml
conda activate microscopy
python src/cli_main.py --help

