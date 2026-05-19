# Data Export Microservice

## What it does
This microservice takes a list of data and saves it as a CSV or JSON file.
You send it a request file, it exports the data, and sends back a response file.

## How to run it
Make sure Python is installed. Then run:
    python microservice.py
The microservice will start and wait for requests.

## How to request data

Create a file called request.json in the same folder with this structure:

    {
        "format": "csv",
        "output_path": "my_export.csv",
        "data": [
            {"ticker": "AAPL", "shares": 10, "price": 189.50},
            {"ticker": "TSLA", "shares": 5,  "price": 245.00}
        ]
    }

format: either "csv" or "json"
output_path: where you want the exported file saved
data: the list of records to export

Example code to send a request:

    import json

    request = {
        "format": "csv",
        "output_path": "my_export.csv",
        "data": [
            {"ticker": "AAPL", "shares": 10, "price": 189.50},
            {"ticker": "TSLA", "shares": 5,  "price": 245.00}
        ]
    }

    with open("request.json", "w") as f:
        json.dump(request, f)

## How to receive data

After the microservice processes your request, it will create a file called response.json.
Read that file to see if it worked.

Example code to receive a response:

    import json, time, os

    while not os.path.exists("response.json"):
        time.sleep(0.1)

    with open("response.json", "r") as f:
        response = json.load(f)

    print(response)

Possible responses:
    {"status": "success", "output_path": "my_export.csv"}
    {"status": "error",   "message": "Missing required fields"}

## UML Sequence Diagram
![UML Diagram](diagram.png)