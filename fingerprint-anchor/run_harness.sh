#!/bin/bash
set -e
echo "=== HonestAGI-style Fingerprint Anchor Verification (10^5 attacks) ==="
cd "$(dirname "$0")"
pip install -r requirements.txt --quiet
python synthetic_test_harness.py
echo "Fingerprint harness complete."
