import requests

url = "http://localhost:5002/pessoa"

x = requests.post(url, data = "XXX")
if x.status_code != 200:
	print(f"[{x.status_code}] {x.text}")
else:
	print(x.text)

h = {"Content-Type": "application/json"}
y = requests.post(url, data = "XXX", headers = h)
if y.status_code != 200:
	print(f"[{y.status_code}] {y.text}")
else:
	print(y.text)

z = requests.post(url, json = {"foo": "bar"})
if z.status_code != 200:
	print(f"[{z.status_code}] {z.text}")
else:
	print(z.text)
 
abc = requests.post(url, json = {"nome": "leozin", "cabelo": "preto", "sexo": "M"})
if abc.status_code != 200:
	print(f"[{abc.status_code}] {abc.text}")
else:
	print(abc.text)