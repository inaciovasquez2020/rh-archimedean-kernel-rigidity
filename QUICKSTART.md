# AKCL Quickstart

This is the shortest path from clone to a first successful AKCL verification pass.

## Requirements

- `git`
- `bash`
- `python3`
- repository Python dependencies

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/rh-archimedean-kernel-rigidity.git
cd rh-archimedean-kernel-rigidity
```

## 2. Check tools

```bash
python3 --version
git --version
```

## 3. Install Python dependencies

```bash
python3 -m pip install -r requirements.txt
```

## 4. Run the canonical truth suite

```bash
make akcl-truth
```

## 5. Next steps

- detailed setup: `docs/SETUP_GUIDE.md`
- contribution policy: `CONTRIBUTING.md`
- canonical status/index: `docs/rigidity/rh/INDEX.md`
