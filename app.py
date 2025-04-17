from flask import Flask, request, Response
import json
from collections import OrderedDict
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Create an OrderedDict to guarantee the correct order of keys
    response_data = OrderedDict([
        ("timestamp", datetime.utcnow().isoformat() + "Z"),  # timestamp first
        ("ip", request.remote_addr)                         # ip second
    ])
    
    # Convert the OrderedDict to a pretty-printed JSON string with indentation
    response_json = json.dumps(response_data, indent=4)
    
    # Return the JSON response with correct order and formatting
    return Response(response_json, mimetype='application/json')

if __name__ == "__main__":
    print("Running Flask app...")
    app.run(host="0.0.0.0", port=5000)
