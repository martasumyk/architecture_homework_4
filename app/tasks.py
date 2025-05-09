from celery import Celery
from logger import log_info

celery = Celery("tasks", broker="redis://redis:6379/0")

@celery.task
def process_message(data):
    log_info(f"Celery is processing message: {data}")
    return f"Processed: {data}"
