#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_metrics(signal, frame):
    # Print metrics when Ctrl+C is pressed or every 10 lines
    global line_count
    line_count += 1
    if line_count % 10 == 0:
        print(f"Total file size: {total_size}")
        for status_code in sorted(status_code_counts.keys()):
            count = status_code_counts[status_code]
            if count > 0:
                print(f"{status_code}: {count}")


# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, print_metrics)

# Process input lines
for line in sys.stdin:
    parts = line.split()
    if len(parts) >= 5:
        try:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except ValueError:
            pass

# Ensure metrics are printed at the end
print_metrics(None, None)
