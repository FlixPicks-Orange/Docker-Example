import requests
import os

def GetThePeople():
    r = requests.get(os.getenv('DB_URL') + "/people")
    return r.json()

def AddPerson(fname, lname):
    data = {
        'fname': fname,
        'lname': lname
    }
    r = requests.post(os.getenv('DB_URL') + "/people", json=data)
    return r