# core/captive.py

import os
import platform
import subprocess
import re

def get_current_gateway():
    try:
        system_platform = platform.system()

        if system_platform == "Windows":
            output = subprocess.check_output("ipconfig", shell=True).decode()
            match = re.search(r"Default Gateway[ .]*: ([\d.]+)", output)
            if match:
                return match.group(1)

        elif system_platform == "Linux":
            output = subprocess.check_output("ip route", shell=True).decode()
            match = re.search(r"default via ([\d.]+)", output)
            if match:
                return match.group(1)

        elif system_platform == "Darwin":  # macOS
            output = subprocess.check_output("netstat -rn", shell=True).decode()
            match = re.search(r"default\s+([\d.]+)", output)
            if match:
                return match.group(1)

        return "Tidak ditemukan gateway"

    except Exception as e:
        return f"Error saat mendeteksi gateway: {e}"
