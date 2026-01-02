# F1 Dashboard

Formula 1 data analysis project using FastF1.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main script:

```bash
python main.py
```

## Features

- Load F1 session data
- Analyze lap times
- Extract driver telemetry data

## Cache

The project uses FastF1's caching feature to store downloaded data locally in the `cache` directory. This speeds up subsequent runs.

## Notes

- First run will download session data (may take a few minutes)
- Subsequent runs will be faster due to caching
- Modify the session parameters in `main.py` to analyze different races/sessions
