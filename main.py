import requests

print("Hello from python!")
response = requests.get("https://api.github.com")
print("Github API status code: ", response.status_code)
