from mongoengine import *


class User(Document):
    fullname = StringField(max_length=150, required=True)
    email = StringField(max_length=150)
    phone = StringField(max_length=50)
    delivery_method = StringField(max_length=50)
    delivered = BooleanField(default=False)

