import json
import os
import time

REQUEST_FILE = "request.json"
RESPONSE_FILE = "response.json"

# some fake stock data to test with
request = {
    "format": "csv",
    "output_path": "portfolio_export.csv",
    "data": [
        {"ticker": "AAPL", "shares": 10, "price": 189.50},
        {"ticker": "TSLA", "shares": 5,  "price": 245.00},
        {"ticker": "GOOG", "shares": 2,  "price": 175.00}
    ]
}

# delete old response file if it exists
if os.path.exists(RESPONSE_FILE):
    os.remove(RESPONSE_FILE)

# send the request
print("Sending request to microservice...")
with open(REQUEST_FILE, "w") as f:
    json.dump(request, f)

# wait for the response
print("Waiting for response...")
timeout = 10
start = time.time()
while not os.path.exists(RESPONSE_FILE):
    if time.time() - start > timeout:
        print("Timed out. Microservice didn't respond.")
        exit()
    time.sleep(0.1)

# read the response
with open(RESPONSE_FILE, "r") as f:
    response = json.load(f)

print("Response received:")
print(response)