import json
from models import User
import connect

user_file = "users.json"


with open(user_file, "r") as fh:
    users = json.load(fh)

if __name__ == '__main__':

    for user in users:
        person = User(fullname=user["fullname"], email=user["email"], phone=user["phone"],
                      delivery_method=user["delivery_method"], delivered=user["delivered"])
        person.save()
