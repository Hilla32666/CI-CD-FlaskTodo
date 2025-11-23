import requests
import sys

url = "http://flask_app:5000/add"


data = {
    "title": "Buy groceries"
}

try:
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Server responded with 200 OK")
        sys.exit(0)
    else:
        print(f"Server responded with {response.status_code}")
        sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)

