"""
cli_main.py

Command-line entry point for the microscopy assembly platform.
"""

import argparse
from core import experiments

def main():
    parser = argparse.ArgumentParser(description="Microscopy Assembly CLI")
    parser.add_argument("--experiment", type=str, default="test",
                        help="Name of experiment to run")
    args = parser.parse_args()

    experiments.run_experiment(args.experiment)

if __name__ == "__main__":
    main()
