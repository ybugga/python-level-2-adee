import requests
import shutil

URL = "https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"
response = requests.get(URL, stream=True)
print(response.status_code)
if response.status_code == 200:
    with open('Examples/data/requests.png', 'wb') as f:
        #print("In here once")
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
elif response.status_code == 403:
    print("Access forbidden. Status code 403.")
    print("Response headers:", response.headers)
    print("Response content:", response.text)