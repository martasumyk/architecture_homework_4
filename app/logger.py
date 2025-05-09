import logging
import os
from datetime import datetime

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def generate_alert(alert_type, description):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"error_reports/{alert_type}_{timestamp}.txt"
    with open(report_path, "w") as f:
        f.write(f"time {timestamp}\n")
        f.write(f"type is {alert_type}\n")
        f.write(f"description is: {description}\n")
