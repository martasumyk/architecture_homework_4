# Homework 4

In this himework we build a simple microservices-based system using: two services that communicate with each other and a logging and alert system.

## Logs + alerts

Every time something happens (like a message being sent), we save a log. I use built-in Python tools and write logs into .txt file in a folder called logs/.

For example, when Service 1 sends a message or when Service 2 receives a message or when a background task starts or finishes - logs help us understand what happened and when — like a history of the system.

On the other hand, if something suspicious happens (like someone trying to send a password), we raise an alert.
How alerts work: if a user sends personal data (e.g. "password", "email", etc.), we detect it and write a mini report inside the error_reports/ folderThe report has: time of the problem and type of alert (e.g. PersonalData) and short description.

## Services

- **Service 1 (`service_1`)**  
  This service is responsible for receiving input from users (e.g., messages or requests). It processes them and passes some data to **Service 2** or a background worker

- **Service 2 (`service_2`)**  
  This service receives requests from Service 1 and simulates doing some processing (e.g., validating, cleaning, or responding)


  ## Celery

  Celery workers handle tasks in the background. For example, if Service 1 gets a message that needs time to process (like analyzing data), it sends that job to Celery and moves on quickly without waiting. Celery picks it up later and does the work.

## Task Flow (Sync vs Async)

Here's how data flows through the system and which parts are **synchronous** and **asynchronous**:

| Step | Action | Service | Type |
|------|--------|---------|------|
| 1 | User sends a message | `service_1` | **Synchronous** |
| 2 | If message is sensitive or invalid | `service_1` logs it + creates alert | **Synchronous** |
| 3 | Normal messages are sent to Celery | Celery via Redis | **Asynchronous** |
| 4 | Celery workers pick up the task | `worker1` or `worker2` | **Asynchronous** |
| 5 | Some messages are forwarded to `service_2` | `service_1` to `service_2` | **Synchronous** |

---
