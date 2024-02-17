import requests
import threading
import time

# Function to send POST request
def send_post_request():
    url = 'http://192.168.234.39'
    while True:
        try:
            response = requests.post(url)
            print(f"Thread {threading.current_thread().name}: POST request sent, Status Code: {response.status_code}")
        except Exception as e:
            print(f"Thread {threading.current_thread().name}: Exception occurred - {str(e)}")
        time.sleep(1)
num_threads = 20
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_post_request, name=f"Thread-{i+1}")
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
