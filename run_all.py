#!/usr/bin/env python3
"""
One-command reproduction script for the revised manuscript.
Runs fingerprint harness + simulation + generates all figures.
"""

import subprocess
import sys

print("=== Running fingerprint harness ===")
subprocess.run(["bash", "fingerprint-anchor/run_harness.sh"], check=True)

print("=== Running simulation (metric d, drift, repair) ===")
subprocess.run([sys.executable, "simulation/drift_simulation.py"], check=True)

print("=== All experiments complete. Figures saved to figures/ and results/ ===")
print("Ready for arXiv upload!")
