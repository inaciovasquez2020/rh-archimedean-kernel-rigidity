PYTHON ?= python3

.PHONY: install test verify surface repo-check

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest

verify:
	$(PYTHON) infra/ci/verify_certificate.py

surface:
	$(PYTHON) -m pytest -q tests/test_repo_surface.py

repo-check:
	sh scripts/run_repo_check.sh

.PHONY: akcl-truth
akcl-truth:
	./scripts/run_akcl_truth_suite.sh
