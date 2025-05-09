import requests
from logger import log_info, generate_alert

def send_message(data):
    log_info(f"Sending data: {data}")
    
    # Check for suspicious input
    if "password" in data.lower():
        generate_alert("PersonalData", f"Attempt to send sensitive data: {data}")
        return

    try:
        r = requests.post("http://service_b:5001/receive", json={"message": data})
        log_info(f"Response from B: {r.text}")
    except Exception as e:
        generate_alert("CommError", str(e))

if __name__ == "__main__":
    send_message("hello from A")
    send_message("my password is 1234")