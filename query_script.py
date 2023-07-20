import time
import random
import requests

while True:
    response = requests.post("http://localhost:5003/method1")
    print(f"Response: {response.status_code}, {response.text}")
    time.sleep(random.randint(1, 5))
