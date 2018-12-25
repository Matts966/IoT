import requests
import json
import setting

ucode = "a304-4"
url = setting.URL
headers = {"Content-Type": "application/json"}
auth = setting.AUTH

putdata_on = {
    'ucode': ucode, # Name or ucode
    'instance': "on"
}
putdata_off = {
    'ucode': ucode,
    'instance': "off"
}

def _put(put_data):
    req = requests.put(url, data=json.dumps(
        putdata), headers=headers, auth=auth)
    return req.status_code

def light_on():
    return _put(putdata_on)

def light_off():
    return _put(putdata_off)

