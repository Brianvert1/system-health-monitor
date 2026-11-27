import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import psutil


def snapshot(interval=1):
    before = psutil.net_io_counters()
    cpu = psutil.cpu_percent(interval=interval)
    after = psutil.net_io_counters()
    return {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'cpu_percent': cpu,
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage(Path.home().anchor).percent,
        'network_sent_bytes_per_second': round((after.bytes_sent-before.bytes_sent)/interval),
        'network_received_bytes_per_second': round((after.bytes_recv-before.bytes_recv)/interval),
    }


def warnings(report, threshold):
    return [f'{key}: {report[key]}% exceeds or meets {threshold}%' for key in
            ('cpu_percent', 'memory_percent', 'disk_percent') if report[key] >= threshold]


def main():
    parser = argparse.ArgumentParser(description='Local system health monitor')
    parser.add_argument('--threshold', type=float, default=85)
    parser.add_argument('--interval', type=float, default=2)
    parser.add_argument('--count', type=int, default=1)
    parser.add_argument('--output', type=Path, default=Path('reports.jsonl'))
    args = parser.parse_args()
    if not 0 < args.threshold <= 100 or args.interval <= 0 or args.count < 1:
        parser.error('Threshold must be 0–100; interval and count must be positive.')
    for _ in range(args.count):
        report = snapshot(args.interval)
        report['warnings'] = warnings(report, args.threshold)
        print(json.dumps(report, indent=2))
        with args.output.open('a', encoding='utf-8') as file:
            file.write(json.dumps(report) + '\n')


if __name__ == '__main__':
    main()
