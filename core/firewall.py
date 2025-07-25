# Kill switch dan firewall logika
# core/firewall.py
import subprocess

def block_suspicious_ports():
    ports_to_block = [135, 137, 138, 139, 445]  # NetBIOS & SMB
    for port in ports_to_block:
        try:
            subprocess.call(f'netsh advfirewall firewall add rule name="Block Port {port}" dir=in action=block protocol=TCP localport={port}', shell=True)
        except Exception as e:
            print(f"[!] Gagal memblokir port {port}: {e}")
