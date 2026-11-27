# IT System Health Monitor

A Python command-line utility for collecting local computer resource metrics and identifying high resource utilization.

## Features
- CPU, RAM and system drive usage monitoring
- Network send and receive rate estimates
- Configurable warning threshold
- Timestamped JSON Lines reports for later analysis

## Getting started
Requires Python 3.10 or newer.

```bash
python -m venv .venv
```
Activate the environment (`.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on macOS/Linux), then run:

```bash
python -m pip install -r requirements.txt
python monitor.py --count 5 --interval 2 --threshold 85
python -m unittest discover -v
```

Reports are appended to `reports.jsonl`. Use `--output` to select another file. Network rates are system-wide estimates, not internet speed tests. High utilization warnings are informational, not a diagnosis.

## Next steps
- Add a dashboard for historical metrics.
- Add per-process resource monitoring.
- Test on additional operating systems.

## Project note
This starter project was developed with AI assistance. Review, test and extend it before presenting it as portfolio work.
