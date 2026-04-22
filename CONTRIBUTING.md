# Contributing to RH Archimedean Kernel Rigidity

## Contribution classes

### 1. Documentation improvements

- clarify repository status
- improve setup instructions
- tighten quickstart commands
- fix ambiguous wording

### 2. Test and truth-suite hardening

- strengthen `make akcl-truth`
- add regression tests
- improve repository-surface checks

### 3. Analytical or semantic changes

These require explicit justification.

- changing AKCL definitions
- changing certificate semantics
- weakening status locks
- expanding theorem claims

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run the canonical truth suite before commit:

```bash
make akcl-truth
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- weakening status locks
- expanding claims without updating status surfaces
