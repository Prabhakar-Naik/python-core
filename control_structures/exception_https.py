
import requests

# http requests

try:
    response = requests.get('valid api uri for getting bulk data')
    response.raise_for_status()  # Raises HTTPError for bad responses
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Request Error:", err)
else:
    print("Request was successful.")
finally:
    print("End of network request handling.")
