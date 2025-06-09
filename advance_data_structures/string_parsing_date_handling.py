# String Parsing and Date Handling
# Write a function that counts how many log entries occurred on each day.
from collections import defaultdict

def count_logs_per_day(timestamps):
    count_by_day = defaultdict(int)
    for ts in timestamps:
        date = ts.split()[0]
        count_by_day[date] += 1
    return dict(count_by_day)

log_times = [
    "2025-06-01 10:23:00", "2025-06-01 12:45:13",
    "2025-06-02 08:15:22", "2025-06-02 09:00:00",
    "2025-06-02 20:31:10"
]

print(count_logs_per_day(log_times))
