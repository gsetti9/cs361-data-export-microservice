import json
import csv
import os
import time

REQUEST_FILE = "request.json"
RESPONSE_FILE = "response.json"

print("Microservice is running. Waiting for requests...")

while True:
    # check if a request file exists
    if os.path.exists(REQUEST_FILE):

        # read the request
        with open(REQUEST_FILE, "r") as f:
            request = json.load(f)

        # delete the request file so to don't process it again
        os.remove(REQUEST_FILE)

        # pull out the pieces needed
        format = request.get("format")
        output_path = request.get("output_path")
        data = request.get("data")

        # check for bad/empty data
        if not data or not format or not output_path:
            response = {"status": "error", "message": "Missing required fields"}

        elif format == "csv":
            try:
                with open(output_path, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                response = {"status": "success", "output_path": output_path}
            except Exception as e:
                response = {"status": "error", "message": str(e)}

        elif format == "json":
            try:
                with open(output_path, "w") as f:
                    json.dump(data, f, indent=2)
                response = {"status": "success", "output_path": output_path}
            except Exception as e:
                response = {"status": "error", "message": str(e)}

        else:
            response = {"status": "error", "message": "Format must be csv or json"}

        # write the response
        with open(RESPONSE_FILE, "w") as f:
            json.dump(response, f)

        print(f"Request processed. Status: {response['status']}")

    time.sleep(0.5)