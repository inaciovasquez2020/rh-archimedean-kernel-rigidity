#!/usr/bin/env bash
set -euo pipefail
python3 -m pytest -q \
  tests/test_akcl_global_rigidity_upgrade_open_problem_literal.py \
  tests/test_akcl_complement_coercivity_open_problem_literal.py \
  tests/test_akcl_complement_defect_dominance_open_problem_literal.py \
  tests/test_akcl_mixed_energy_leakage_open_problem_literal.py \
  tests/test_akcl_mixed_defect_leakage_open_problem_literal.py \
  tests/test_akcl_spectral_radius_verification_open_problem_literal.py \
  tests/test_akcl_global_rigidity_upgrade_registry_literal.py \
  tests/test_akcl_global_rigidity_upgrade_truth_sync.py \
  tests/test_akcl_completion_snapshot_literal.py \
  tests/test_akcl_completion_truth_sync.py \
  tests/test_akcl_index_literal.py \
  tests/test_readme_akcl_index_entrypoint_literal.py
