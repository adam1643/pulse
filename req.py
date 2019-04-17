import requests
import json

MAIN_URL = "http://localhost:8090/api/v1/users"


def save_pulse(pulse, userid, username, password):
    url = MAIN_URL + "/" + userid + "/pulses"
    data = {"pulse": pulse}
    headers = {"Content-Type": "application/json"}
    req = requests.post(url, data=json.dumps(data), headers=headers, auth=(username, password))
    return req


def get_pulse(userid, username, password):
    url = MAIN_URL + "/" + userid + "/pulses"
    req = requests.get(url, auth=(username, password))
    return req


uid = "5cb5b4fc3d9f053c8d90262d"
(usr, pwd) = ("abc", "abc")

a = get_pulse(userid=uid, username=usr, password=pwd)
b = save_pulse(pulse=73, userid=uid, username=usr, password=pwd)
print(a.text)
print(b.text)
