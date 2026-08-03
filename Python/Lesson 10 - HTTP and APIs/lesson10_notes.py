import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)

# print(response.text)
# print(response.headers["content-type"])
# print(response.elapsed)
# print(response.reason)
# print(response.status_code)

BASE_URL = "https://httpbin.org"

headers = {"Authorization": "Bearer abc123"}
response = requests.get(f"{BASE_URL}/bearer", headers=headers)

print(response.status_code)
print(response.json())