# Setup Guide

This guide is for contributors who want a reliable local environment for the AKCL repository.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/rh-archimedean-kernel-rigidity.git
cd rh-archimedean-kernel-rigidity
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Fast verification pass

```bash
make akcl-truth
```

## Focused Python test pass

```bash
python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
make akcl-truth
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `docs/rigidity/rh/INDEX.md`
