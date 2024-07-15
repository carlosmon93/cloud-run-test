import requests

# The API endpoint
url = "TBD"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json)

"""
"""