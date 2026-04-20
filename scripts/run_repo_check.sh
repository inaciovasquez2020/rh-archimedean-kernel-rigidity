#!/bin/sh
set -eu

python3 -m pytest -q
python3 infra/ci/verify_certificate.py
