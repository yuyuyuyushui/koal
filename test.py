import requests
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/1234567890')
r = s.get("http://httpbin.org/cookies")

print(r.text)