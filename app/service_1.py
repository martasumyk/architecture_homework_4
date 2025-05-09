from tasks import process_message
from logger import log_info, generate_alert

def send_message(data):
    log_info(f"Task for data: {data}")

    if "password" in data.lower():
        generate_alert("PersonalData", f"Attempt to send sensitive data: {data}")
        return

    task = process_message.delay(data)
    log_info(f"Task sent to celery with ID: {task.id}")
