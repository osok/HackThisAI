import requests

r = requests.post("http://localhost:5000/predict", json={"oc":1, 'hl':2, 'vol':3})
print(r.text)
'''
# Once you've build a model, compare it to the original
with open("test/test_user.py", "rb") as f:
    r = requests.post("http://localhost:5000/check", files={"data_file": f})
    print(r.text)
'''