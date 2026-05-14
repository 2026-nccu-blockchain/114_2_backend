# HOTEL System

## Setup

### 1) Create a virtual environment

```bash
python -m venv .venv
```

### 2) Activate the environment

```bash
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Setup env file

```bash
cp app/.env.example app/.env
```

## Before Run

please check env is already rewriten

## Run

```bash
uvicorn app.main:app --reload
```


testing2
