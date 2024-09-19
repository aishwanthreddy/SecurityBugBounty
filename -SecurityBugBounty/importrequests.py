import requests
import os

# API Testing Parameters
api_url = 'https://your-api-endpoint.com/resource'
payloads = ["' OR '1'='1", "' OR '1'='2", "' OR 'x'='x"]

# Function to test API with different payloads
def test_api_vulnerabilities():
    for payload in payloads:
        params = {'search': payload}
        response = requests.get(api_url, params=params)
        print(f'Payload: {payload}\nStatus Code: {response.status_code}\nResponse: {response.text}\n')

# Function to find hardcoded secrets in decompiled APK files
def find_hardcoded_secrets(directory):
    keywords = ['api_key', 'password', 'secret']
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    for keyword in keywords:
                        if keyword in content:
                            print(f'Found {keyword} in {file_path}')
            except Exception as e:
                print(f'Error reading {file_path}: {e}')

# Main function to run both tests
def main():
    print("Starting API vulnerability testing...")
    test_api_vulnerabilities()
    
    print("Starting hardcoded secrets search...")
    # Replace 'output_directory' with the directory where the APK was decompiled
    find_hardcoded_secrets('output_directory')

if __name__ == '__main__':
    main()
