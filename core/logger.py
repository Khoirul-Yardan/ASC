# Logging ke file
# core/logger.py
import datetime

def log_event(message, log_file="log/alert_log.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as log:
        log.write(f"[{timestamp}] {message}\n")
