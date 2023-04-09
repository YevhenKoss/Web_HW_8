import pika

from database import connect
from database.models import User


credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
channel = connection.channel()

users = User.objects()

# channel.exchange_declare(exchange="", exchange_type="direct")
channel.queue_declare(queue="email_queue")
channel.queue_declare(queue="sms_queue")

for user in users:
    if user.delivery_method == "SMS":
        message = str(user.id).encode()
        channel.basic_publish(exchange="", routing_key="sms_queue", body=message)
        print(f"[x] Sent message: {message}")
    elif user.delivery_method == "email":
        message = str(user.id).encode()
        channel.basic_publish(exchange="", routing_key="email_queue", body=message)
        print(f"[x] Sent message: {message}")

connection.close()
