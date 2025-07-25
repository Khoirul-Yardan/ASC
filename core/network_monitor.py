# core/network_monitor.py

import time
import socket
from core.alert import send_telegram_alert
from core.logger import log_event
from core.captive import get_current_gateway

def monitor_network(check_interval=5):
    last_gateway = get_current_gateway()
    log_event(f"Monitoring dimulai. Gateway awal: {last_gateway}")

    while True:
        current_gateway = get_current_gateway()
        if current_gateway != last_gateway:
            message = f"🚨 *Peringatan!* Gateway berubah dari {last_gateway} ke {current_gateway}"
            send_telegram_alert(message)
            log_event(f"Gateway berubah dari {last_gateway} ke {current_gateway}")
            last_gateway = current_gateway
        time.sleep(check_interval)
