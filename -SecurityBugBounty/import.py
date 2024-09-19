import os

def find_hardcoded_secrets(directory):
    keywords = ['api_key', 'password', 'secret']
    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), 'r', errors='ignore') as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        print(f'Found {keyword} in {file}')

# Replace 'output_directory' with the directory where the APK was decompiled
find_hardcoded_secrets('output_directory')
